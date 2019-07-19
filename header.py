def header():
    reader = open("default/header.txt", "r")
    head = reader.read()
    reader.close()

    return head