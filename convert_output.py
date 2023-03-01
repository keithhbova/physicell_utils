import os
import subprocess

listOfMatlabFiles = []

path = "output"
for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".mat")):
            currentFile = os.path.join(root,file)
            if(currentFile.split("_")[1] == "cells.mat"):
                listOfMatlabFiles.append(currentFile)

listOfMatlabFiles.sort()

listOfMatlabFiles.pop(0)



os.mkdir("results")
os.mkdir("results/output")

for file in listOfMatlabFiles:
    newName = "results/" + file.split("_")[0] + "_cells_physicell.mat"
    subprocess.call(f"cp {file} {newName}", shell=True)


