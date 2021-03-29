# Windows Event Viewer _`(python)`_

## Descrição

Ferramenta criada para listar e analisar todos os logs de eventos do sistema operacional _windows_ por meio de tabelas.

> ![Demo](wev_demo.gif)

## Tecnologias Utilizadas

> __`Python 3.7.0`:__
>- _Eel_          (Integração de Interface HTML+CSS+JAVASCRIPT(Cliente) e Python(Servidor))
>- _Evtx_         (Conversão de .evtx para .json)
>- _Pandas_       (Conversão de .json para DataFrame e realização de filtros)
>- _Pyinstaller_  (Criação do .exe apartir do codigo python)

## Configurações Iniciais

1. `git clone https://github.com/sql3t0/WindowsEventViewer.git`
2. `cd WindowsEventViewer`
3. `python3 -m pip install -r requirements.txt`

## Criar Binario _`(.exe)`_

- Gerar com console:
```ruby
{PYTHON_FOLDER}\\Scripts\\pyinstaller.exe WinEventView.py --icon=event.ico --hidden-import bottle_websocket --add-data "{PYTHON_FOLDER}\\lib\\site-packages\\eel\\eel.js;eel" --uac-admin --onefile
```
> Release: [WinEventView.VisibleConsole](https://github.com/sql3t0/WindowsEventViwer/releases/download/v1.0/WinEventView.VisibleConsole.exe)

- Gerar sem console:
```ruby
{PYTHON_FOLDER}\\Scripts\\pyinstaller.exe WinEventView.py --icon=event.ico --hidden-import bottle_websocket --add-data "{PYTHON_FOLDER}\\lib\\site-packages\\eel\\eel.js;eel" --uac-admin --onefile --noconsole
```
> Release: [WinEventView](https://github.com/sql3t0/WindowsEventViwer/releases/download/v1.0/WinEventView.exe)

## Executar

- Usando _`python`_:
```ruby
python3 .\\WinEventView.py
```

- Usando o _`.exe`_:
```ruby
.\\dist\\WinEventView.exe
```
