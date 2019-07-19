def intro():
    reader = open("intro.txt", "r")
    data = reader.read()
    reader.close()
    print(data)
