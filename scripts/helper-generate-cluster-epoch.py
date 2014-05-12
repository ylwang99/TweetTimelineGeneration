# This file is to generate corresponding epoch files from representatives for convert-epoch-to-js.pl
# to convert to js file so that it can be fed into timeline visualization

from sets import Set
import os
import sys

path_data = "../data/timeline-representatives/"
path_epoch = sys.argv[1]

if os.path.exists(path_epoch):
    os.remove(path_epoch)

dirs = os.listdir(path_data)
file_epoch = open(path_epoch, "a")
for file in dirs:
    if file[-4:] == ".txt":
        file_data = open(path_data + file, "r")
        representatives = Set()
        lines = file_data.readlines()
        for line in lines:
            line = line.strip().split()
            representatives.add(line[0])
        file_data.close()
        file_qrels = open("../data/qrels-microblog-epoch.txt", "r")
        lines = file_qrels.readlines()
        for line in lines:
            line = line.strip().split()
            topicNum = int(file[:file.index(".")])
            if topicNum < 100:
                topic = "MB%02d" % topicNum
            else:
                topic = "MB%d" % topicNum 
            if line[0] == topic and int(line[3]) > 0:
                if line[2] in representatives:
                    file_epoch.write(line[0] + " " + line[1] + " " + line[2] + " 2 " + line[4] + " " + line[5] + "\n")
                else:
                    file_epoch.write(line[0] + " " + line[1] + " " + line[2] + " 1 " + line[4] + " " + line[5] + "\n")
        file_qrels.close()
file_epoch.close()