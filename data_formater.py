def data_formater(config):
    lines = []
    for appname in config:
        route = config.get(appname)[0].get('address')
        type = returnvalue = config.get(appname)[0].get('type')
        returnvalue = config.get(appname)[0].get('result')
        if (type == "return"):
            route = "@app.route(\"" + route + "\")\n"
            function = "def " + str(appname) + "():\n\treturn(\"" + str(returnvalue) + "\")\n"
        elif (type == "return-page"):
            route = "@app.route(\"" + route + "\")\n"
            function = "def " + str(appname) + "():\n\tcontent = get_file(\"" + str(returnvalue) + \
                       "\")\n\treturn Response(content, mimetype =\"text/html\")\n"

        lines.append(route)
        lines.append(function)

    return lines