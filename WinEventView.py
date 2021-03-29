#!/usr/bin/env python3
import io
import eel
import json
import glob
import index
import os,sys
import hashlib
import threading
import pandas as pd
from js_css import DATA
from zipfile import ZipFile
from typing import Collection
from evtx import PyEvtxParser

# Global variables
DEFAULT_DIR_RUN = os.path.abspath(os.getcwd())
CONFIG_FILENAME = 'config.json'

def error(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(e,exc_type, fname, exc_tb.tb_lineno)

@eel.expose
def saveEditConf(CONFIG_DATA):
    global CONFIG_FILENAME, WIN_LOG_PATH, IGNORE_COLUMN, REG_COUNT_LIMIT, REGEX_PATERN
    try:
        with open(CONFIG_FILENAME, 'w') as data:
            json.dump(CONFIG_DATA, data, indent=4)
        
        WIN_LOG_PATH, IGNORE_COLUMN, REG_COUNT_LIMIT, REGEX_PATERN, SERVER_HOST, SERVER_PORT = loadconf(CONFIG_FILENAME)
        eel.alertx("Settings saved successfully")
    except Exception as e:
        error(e)
        eel.alertx(f"Error trying to save settings !\n {e}")


def createDefaultconf(CONFIG_FILENAME):
    with open(CONFIG_FILENAME, 'w') as data:
        json.dump({"WIN_LOG_PATH":"\\\\localhost\\C$\\Windows\\System32\\winevt\\Logs\\*.evtx", "IGNORE_COLUMN":["xmlns"], "REG_COUNT_LIMIT": 20, "REGEX_PATERN":".*", "SERVER_HOST":"localhost", "SERVER_PORT": 8000}, data, indent=4)

def loadconf(CONFIG_FILENAME):
    try:
        with open(CONFIG_FILENAME) as json_file:
            data = json.load(json_file)

        return data['WIN_LOG_PATH'], data['IGNORE_COLUMN'], int(data['REG_COUNT_LIMIT']), data['REGEX_PATERN'], data['SERVER_HOST'], int(data['SERVER_PORT'])
    except Exception as e:
        # error(e)
        createDefaultconf(CONFIG_FILENAME)
        return loadconf(CONFIG_FILENAME)

# Global values from config.json
WIN_LOG_PATH, IGNORE_COLUMN, REG_COUNT_LIMIT, REGEX_PATERN, SERVER_HOST, SERVER_PORT = loadconf(CONFIG_FILENAME)

def readXmlObj(obj,EVTx):
    for key in obj.keys():
        try:
            readXmlObj(obj[key],EVTx)
        except Exception as e:
            # print(key,':',obj[key],type(obj[key]))    #verbose
            if key in IGNORE_COLUMN:
                pass
            else:
                if  isinstance(obj[key], list):
                    obj[key] = ', '.join(obj[key])

                if key in EVTx:
                    newKey = f'{key}_{len(EVTx[key])}'
                    EVTx[newKey] = [obj[key]]
                else:
                    EVTx[key] = [obj[key]]
    return EVTx

def createDir(name):
    try:
        if not os.path.isdir(name):
            os.mkdir(name)    
        return name
    except Exception as e:
        error(e)


def filename(file):
    try:
        filepath, filename = os.path.split(file)
        return filename
    except Exception as e:
        error(e)

def md5(x):
    try:
        return hashlib.md5(x.encode('utf-8')).hexdigest()
    except Exception as e:
        error(e)

def asyncGenLogs(file):
    EVTx = {}
    json_data_dir = createDir('web\json_data')
    print('EVTxFILE:',file)
    
    fname = filename(file)
    _df = pd.DataFrame()
    parser = PyEvtxParser(file)
    
    i = 0   # Register counter
    for record in parser.records_json():
        data = json.loads(record['data'])['Event']
        readXmlObj(data,EVTx)
        try:
            df = pd.DataFrame.from_dict(EVTx).fillna(0)
            _df = _df.append(df)
            i+=1
        except Exception as e:
            pass

        EVTx = {}
        if i > (REG_COUNT_LIMIT-1):
            break

        
    if not _df.empty:
        if REGEX_PATERN:
            try:
                _df = _df[_df.apply(lambda x: x.astype(str).str.contains(REGEX_PATERN, case=False, na=False)).any(axis=1)]
            except Exception as e:
                # error(e)  #verbose
                pass

        _df = _df.set_index('EventRecordID').sort_values(by=['EventRecordID'], ascending=False)
        _df.to_json(f'{json_data_dir}\\{md5(fname)}.json', orient="table")
        r, c = _df.shape
        eel.feedback(f'Lines: {r}, Columns: {c}', md5(file))
    else:
        pd.DataFrame(['Empty'],columns=['File']).to_json(f'{json_data_dir}\\{md5(fname)}.json', index=False, orient="table")
        eel.feedback(f'Empty', md5(file))


@eel.expose
def genLogs(file):
    try:
        threading.Thread(target=asyncGenLogs,args=(file,)).start()
    except Exception as e:
        error(e)

def unpackJsCss(web_path):
    try:
        with ZipFile(io.BytesIO(DATA), 'r') as zipObj:
            zipObj.extractall(web_path)
    except Exception as e:
        error(e)

if __name__ == "__main__":
    web_path = createDir(f'{DEFAULT_DIR_RUN}\\web')
    unpackJsCss(web_path)
    CHECKS_OPTIONS = '';SELECT_OPTIONS='';i=0
    for file in glob.glob(WIN_LOG_PATH):
        SELECT_OPTIONS += f'<option value="{md5(filename(file))}" id="OPT{i}">{file}</option>'
        CHECKS_OPTIONS += f'<tr onclick="checkSelect(\'inp_{md5(file)}\')"><td width="5%"><input id="inp_{md5(file)}" onclick="checkSelect(\'inp_{md5(file)}\')" class="form-check-input select-all" type="checkbox" value="{file}"></td><td>{file}</td><td class="text-center" id="{md5(file)}"></td></tr>'
        i+=1

    with open(f'{web_path}\\index.html', 'w', encoding='utf-8') as file:
        file.write(index.create([WIN_LOG_PATH, IGNORE_COLUMN, REG_COUNT_LIMIT, REGEX_PATERN, SERVER_HOST, SERVER_PORT], SELECT_OPTIONS, CHECKS_OPTIONS))

    eel.init(web_path)
    eel.start('index.html', host=SERVER_HOST, port=SERVER_PORT)
