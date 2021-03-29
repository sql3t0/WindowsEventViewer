#!/usr/bin/env python3

def create(CONFIG, SELECT_OPTIONS, CHECKS_OPTIONS):
    
    CSS = '''
    body { font-size: 12px;}
    td { white-space: normal !important;}
    #tbgenlogs tbody { display:block; max-height:460px; overflow-y:scroll; }
    #tbgenlogs thead, #tbgenlogs tbody tr { display:table; width:100%; table-layout:fixed; }
    #modaleditconfig { display:block; max-height:460px; overflow-y:scroll; }
    '''
    
    JSCRIPT='''
    function getDT(FILENAME) {
        $("#MyTable").remove();
        $("#datatable").html('<table id="MyTable" class="display responsive cell-border w-auto table-sm" style="width:100%"></table>');
        
        FILENAME = "json_data/"+FILENAME+".json"
        var columns = [];
        $.ajax({
            url: FILENAME,
            success: function (data) {
                console.log(data);
                data = JSON.parse(JSON.stringify(data));
                columnNames = Object.keys(data.data[0]);
                for (var i in columnNames) {
                    columns.push({data: columnNames[i], 
                    title: capitalizeFirstLetter(columnNames[i])});
                }
                $('#MyTable').DataTable({
                    order: [0, 'desc'],
                    dom: 'Bfrtip',
                    keys: true,
                    select: true,
                    colReorder: true,
                    buttons: [
                        'colvis',
                        {
                            extend: 'searchBuilder',
                            config: {
                                depthLimit: 2
                            }
                        }
                        ,'copy', 'excel', 'pdf'
                    ],
                    data: data.data,
                    columns: columns
                } );
            }
        });
    }

    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

    eel.expose(feedback);
    function feedback(txt,id){
        $("#"+id).html(txt);
    }

    eel.expose(alertx);
    function alertx(txt){
        alert(txt);
    }

    $("#selectAll").change(function () {
        var checked = this.checked;
        $("input.select-all").each(function (index,item) {
            item.checked = checked;
            if(item.checked){
                $(".form-check-input").prop("disabled", false);
            }else{
                $(".form-check-input").prop('checked', false);
            }
        });
    });

    var MD5 = function(d){var r = M(V(Y(X(d),8*d.length)));return r.toLowerCase()};function M(d){for(var _,m="0123456789ABCDEF",f="",r=0;r<d.length;r++)_=d.charCodeAt(r),f+=m.charAt(_>>>4&15)+m.charAt(15&_);return f}function X(d){for(var _=Array(d.length>>2),m=0;m<_.length;m++)_[m]=0;for(m=0;m<8*d.length;m+=8)_[m>>5]|=(255&d.charCodeAt(m/8))<<m%32;return _}function V(d){for(var _="",m=0;m<32*d.length;m+=8)_+=String.fromCharCode(d[m>>5]>>>m%32&255);return _}function Y(d,_){d[_>>5]|=128<<_%32,d[14+(_+64>>>9<<4)]=_;for(var m=1732584193,f=-271733879,r=-1732584194,i=271733878,n=0;n<d.length;n+=16){var h=m,t=f,g=r,e=i;f=md5_ii(f=md5_ii(f=md5_ii(f=md5_ii(f=md5_hh(f=md5_hh(f=md5_hh(f=md5_hh(f=md5_gg(f=md5_gg(f=md5_gg(f=md5_gg(f=md5_ff(f=md5_ff(f=md5_ff(f=md5_ff(f,r=md5_ff(r,i=md5_ff(i,m=md5_ff(m,f,r,i,d[n+0],7,-680876936),f,r,d[n+1],12,-389564586),m,f,d[n+2],17,606105819),i,m,d[n+3],22,-1044525330),r=md5_ff(r,i=md5_ff(i,m=md5_ff(m,f,r,i,d[n+4],7,-176418897),f,r,d[n+5],12,1200080426),m,f,d[n+6],17,-1473231341),i,m,d[n+7],22,-45705983),r=md5_ff(r,i=md5_ff(i,m=md5_ff(m,f,r,i,d[n+8],7,1770035416),f,r,d[n+9],12,-1958414417),m,f,d[n+10],17,-42063),i,m,d[n+11],22,-1990404162),r=md5_ff(r,i=md5_ff(i,m=md5_ff(m,f,r,i,d[n+12],7,1804603682),f,r,d[n+13],12,-40341101),m,f,d[n+14],17,-1502002290),i,m,d[n+15],22,1236535329),r=md5_gg(r,i=md5_gg(i,m=md5_gg(m,f,r,i,d[n+1],5,-165796510),f,r,d[n+6],9,-1069501632),m,f,d[n+11],14,643717713),i,m,d[n+0],20,-373897302),r=md5_gg(r,i=md5_gg(i,m=md5_gg(m,f,r,i,d[n+5],5,-701558691),f,r,d[n+10],9,38016083),m,f,d[n+15],14,-660478335),i,m,d[n+4],20,-405537848),r=md5_gg(r,i=md5_gg(i,m=md5_gg(m,f,r,i,d[n+9],5,568446438),f,r,d[n+14],9,-1019803690),m,f,d[n+3],14,-187363961),i,m,d[n+8],20,1163531501),r=md5_gg(r,i=md5_gg(i,m=md5_gg(m,f,r,i,d[n+13],5,-1444681467),f,r,d[n+2],9,-51403784),m,f,d[n+7],14,1735328473),i,m,d[n+12],20,-1926607734),r=md5_hh(r,i=md5_hh(i,m=md5_hh(m,f,r,i,d[n+5],4,-378558),f,r,d[n+8],11,-2022574463),m,f,d[n+11],16,1839030562),i,m,d[n+14],23,-35309556),r=md5_hh(r,i=md5_hh(i,m=md5_hh(m,f,r,i,d[n+1],4,-1530992060),f,r,d[n+4],11,1272893353),m,f,d[n+7],16,-155497632),i,m,d[n+10],23,-1094730640),r=md5_hh(r,i=md5_hh(i,m=md5_hh(m,f,r,i,d[n+13],4,681279174),f,r,d[n+0],11,-358537222),m,f,d[n+3],16,-722521979),i,m,d[n+6],23,76029189),r=md5_hh(r,i=md5_hh(i,m=md5_hh(m,f,r,i,d[n+9],4,-640364487),f,r,d[n+12],11,-421815835),m,f,d[n+15],16,530742520),i,m,d[n+2],23,-995338651),r=md5_ii(r,i=md5_ii(i,m=md5_ii(m,f,r,i,d[n+0],6,-198630844),f,r,d[n+7],10,1126891415),m,f,d[n+14],15,-1416354905),i,m,d[n+5],21,-57434055),r=md5_ii(r,i=md5_ii(i,m=md5_ii(m,f,r,i,d[n+12],6,1700485571),f,r,d[n+3],10,-1894986606),m,f,d[n+10],15,-1051523),i,m,d[n+1],21,-2054922799),r=md5_ii(r,i=md5_ii(i,m=md5_ii(m,f,r,i,d[n+8],6,1873313359),f,r,d[n+15],10,-30611744),m,f,d[n+6],15,-1560198380),i,m,d[n+13],21,1309151649),r=md5_ii(r,i=md5_ii(i,m=md5_ii(m,f,r,i,d[n+4],6,-145523070),f,r,d[n+11],10,-1120210379),m,f,d[n+2],15,718787259),i,m,d[n+9],21,-343485551),m=safe_add(m,h),f=safe_add(f,t),r=safe_add(r,g),i=safe_add(i,e)}return Array(m,f,r,i)}function md5_cmn(d,_,m,f,r,i){return safe_add(bit_rol(safe_add(safe_add(_,d),safe_add(f,i)),r),m)}function md5_ff(d,_,m,f,r,i,n){return md5_cmn(_&m|~_&f,d,_,r,i,n)}function md5_gg(d,_,m,f,r,i,n){return md5_cmn(_&f|m&~f,d,_,r,i,n)}function md5_hh(d,_,m,f,r,i,n){return md5_cmn(_^m^f,d,_,r,i,n)}function md5_ii(d,_,m,f,r,i,n){return md5_cmn(m^(_|~f),d,_,r,i,n)}function safe_add(d,_){var m=(65535&d)+(65535&_);return(d>>16)+(_>>16)+(m>>16)<<16|65535&m}function bit_rol(d,_){return d<<_|d>>>32-_}
    var spin = '<div class="text-center"><div class="spinner-border spinner-border-sm text-secondary" role="status"> <span class="visually-hidden">Loading...</span></div></div>'
    async function genLogs(x){
        eel.genLogs(x);
    }
    $("#genlogs" ).click(function() {
        $("input.select-all").each(function (index,item) {
            if(item.checked){
                feedback(spin,MD5(item.value));
                genLogs(item.value);
            }
        });
    });
    
    $("#btsaveconfig" ).click(function() {
        data = {"WIN_LOG_PATH": $('#formeditconfig input#WIN_LOG_PATH').val(), "IGNORE_COLUMN": eval($('#formeditconfig textarea#IGNORE_COLUMN').val()), "REG_COUNT_LIMIT": $('#formeditconfig input#REG_COUNT_LIMIT').val(), "REGEX_PATERN": $('#formeditconfig textarea#REGEX_PATERN').val(), "SERVER_HOST":$('#formservereditconfig input#SERVER_HOST').val(), "SERVER_PORT":$('#formservereditconfig input#SERVER_PORT').val() };
        eel.saveEditConf(data);
    });

    function checkSelect(id){
        if($("#"+id).is(':checked')){
            $("#"+id).prop('checked', false); 
        }else{
            $("#"+id).prop('checked', true);
        }
    }
    '''

    HTML = f'''
    <!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="css/datatables.min.css"/>
            <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css"/>
            
            <script type="text/javascript" src="js/pdfmake.min.js"></script>
            <script type="text/javascript" src="js/vfs_fonts.js"></script>
            <script type="text/javascript" src="js/datatables.min.js"></script>
            <script type="text/javascript" src="js/bootstrap.bundle.min.js"></script>
            <script type="text/javascript" src="eel.js"></script>

            <meta charset=utf-8 />
            <title>Windows Event Analizer</title>
            <style>{CSS}</style>
        </head>
        <body>
            <div class="container-fluid">
                <div class="row mt-3">
                    <div class="col-8">
                        <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" onchange="getDT(this.value)">
                            <option selected>Select a Log...</option>
                            {SELECT_OPTIONS}
                        </select>
                    </div>
                    <div class="col-3">
                        <!-- Button trigger modal -->
                        <button type="button" class="btn btn-outline-secondary btn-lg" data-bs-toggle="modal" data-bs-target="#exampleModal" style="width: 100% !important">
                            Generate Logs
                        </button>

                        <!-- Modal -->
                        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog modal-xl">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">Available Logs</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div id="modalgenlogs" class="modal-body">
                                        <div class="table-responsive">
                                            <table id="tbgenlogs" class="table table-sm table-striped table-hover w-auto">
                                                <thead>
                                                    <tr>
                                                        <th width="5%">
                                                            <div class="form-check" width="5%">
                                                                <input id="selectAll" class="form-check-input" type="checkbox" value="">
                                                            </div>
                                                        </th>
                                                        <th><div class="form-check">Log File</div></th>
                                                        <th><div class="form-check text-center">Registers</div></th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    {CHECKS_OPTIONS}
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" id="genlogs" class="btn btn-primary">Generate</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-1">
                        <!-- Button trigger modal -->
                        <button type="button" class="btn btn-outline-secondary" data-bs-toggle="modal" data-bs-target="#exampleModal1" style="width: 100% !important">
                            <img width="34" height="34" src="data:image/png;base64,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" />
                        </button>

                        <!-- Modal -->
                        <div class="modal fade" id="exampleModal1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog modal-xl">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">Settings</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div id="modaleditconfig" class="modal-body">
                                        <form id="formeditconfig">
                                            <div class="row m-1"> 
                                                <div class="form-group col-md-9 mt-2">
                                                    <label for="WIN_LOG_PATH" class="mb-1">Windows event logs directory:</label>
                                                    <input type="text" class="form-control form-control" id="WIN_LOG_PATH" value="{CONFIG[0]}" placeholder="E.g: \\\\localhost\\C$\\Windows\\System32\\winevt\\Logs\\*.evtx">
                                                </div>
                                                <div class="form-group col-md-3 mt-2">
                                                    <label for="REG_COUNT_LIMIT" class="mb-1">Generate the last 'N' records</label>
                                                    <input type="text" class="form-control form-control" id="REG_COUNT_LIMIT" value="{CONFIG[2]}" placeholder="E.g: 100">
                                                </div>
                                            </div>
                                            <div class="row m-1">
                                                <div class="form-group mt-2">
                                                    <label for="IGNORE_COLUMN" class="mb-1">Ignore these columns: </label>
                                                    <textarea class="form-control form-control" id="IGNORE_COLUMN" rows="3" placeholder="E.g: ['xmlns','name','channel']">{CONFIG[1]}</textarea>
                                                </div>
                                                <div class="form-group mt-2">
                                                    <label for="REGEX_PATERN" class="mb-1">Generate lines that contain these words:</label>
                                                    <textarea class="form-control form-control" id="REGEX_PATERN" rows="3" placeholder="E.g: 192.168.1.1|test|myword|192.168.[01].[0-100]">{CONFIG[3]}</textarea>
                                                    <small id="REGEX_PATERN_Help" class="form-text text-muted"> Case-insensitive and pipe-separated. </small>
                                                </div>
                                            </div>
                                        </form>
                                        <div class="conteiner card mt-3">
                                            <div class="card-header">
                                                Server Settings
                                            </div>
                                            <div class="card-body">
                                                <form class="form" id="formservereditconfig">  
                                                    <div class="row">
                                                        <div class="form-group col-md-8">
                                                            <label for="SERVER_HOST" class="mb-1">Host</label>
                                                            <input type="text" class="form-control" id="SERVER_HOST" value="{CONFIG[4]}" placeholder="E.g: 192.168.0.2">
                                                        </div>
                                                        <div class="form-group col-md-4">
                                                            <label for="SERVER_PORT" class="mb-1">Port</label>
                                                            <input type="text" class="form-control" id="SERVER_PORT" value="{CONFIG[5]}" placeholder="E.g: 9090">
                                                        </div>
                                                    </div>
                                                </form>
                                            </div>
                                            <div class="container mb-3">
                                                <small id="SERVER_SETTINGS_Help" class="form-text text-danger"> *Changes made to the server settings will only be valid after restarting the application. </small>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                        <button type="button" id="btsaveconfig" class="btn btn-primary">Save Changes</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                        <p id="datatable" class="card-text">
                            
                        </p>
                    </div>
                </div>
            </div>
            <script>
                {JSCRIPT}
            </script>
        </body>
    </html>
    '''
    return HTML