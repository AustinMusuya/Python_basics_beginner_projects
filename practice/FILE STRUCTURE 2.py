import os

directory = os.path.normpath("D:/myfiles")
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".txt"):
            f = open(os.path.join(subdir, file), "r")
            a = f.read()
            print(a)
            f.close()
