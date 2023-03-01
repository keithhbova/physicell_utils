import os
import subprocess

listOfPovFiles = []

path = "."
for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".pov")):
            currentFile = os.path.join(root,file)
            listOfPovFiles.append(currentFile)

listOfPovFiles.sort()


for file in listOfPovFiles:
    subprocess.call(f"povray {file}", shell=True)


