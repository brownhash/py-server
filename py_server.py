from intro import intro
from header import header
from footer import footer
from create_server import create_server
from config_reader import config_reader
from data_formater import data_formater
import os
import time

timestamp = str(time.strftime("%d:%m:%y-%H:%M:%S"))

intro()
config = config_reader()
lines = data_formater(config)
for appname in config:
    route = config.get(appname)[0].get('address')
    type = returnvalue = config.get(appname)[0].get('type')
    returnvalue = config.get(appname)[0].get('result')
    if(type == "return"):
        route = "@app.route(\""+route+"\")\n"
        function = "def "+str(appname)+"():\n\treturn(\""+str(returnvalue)+"\")\n"
    elif(type == "return-page"):
        route = "@app.route(\"" + route + "\")\n"
        function = "def " + str(appname) + "():\n\tcontent = get_file(\"" + str(returnvalue) + \
                   "\")\n\treturn Response(content, mimetype =\"text/html\")\n"

    lines.append(route)
    lines.append(function)
lines = data_formater(config)
data = ""
for i in lines:
    data += i
create_server(header(), footer(), data)

log = open("output.log",'a')
log.write("Server started at: "+timestamp+"\n")
log.close()

os.system("python3 server.py")
