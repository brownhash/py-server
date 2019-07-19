def footer():
    reader = open("default/footer.txt", "r")
    foot = reader.read()
    reader.close()

    return foot