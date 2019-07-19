def create_server(header,footer,data):
    writer = open("server.py","w")
    writer.write(header)
    writer.write("\n"+data+"\n")
    writer.write(footer)
    writer.close()