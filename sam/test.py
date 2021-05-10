import os

dir_name = "." # Edit as needed


for parent, dirnames, filenames in os.walk(dir_name): 
    for fn in filenames:
        f = open(os.path.join(parent, fn), 'a')
        f.write("\ntext\n")
        f.close()
text
