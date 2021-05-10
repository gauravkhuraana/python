with open("abc.txt", 'r+') as fp:
    lines = fp.readlines()     # lines is list of line, each element '...\n'
    lines.insert(0, "sam\n hello hi okji\n aaye ho merei jindai mein \n tum bahara banke ")  # you can use any index if you know the line index
    fp.seek(0)                 # file pointer locates at the beginning to write the whole file again
    fp.writelines(lines)     