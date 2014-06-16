# This file is to generate corresponding epoch files from representatives for convert-epoch-to-js.pl
# to convert to js file so that it can be fed into timeline visualization

from sets import Set
import os
import sys
import json

path_clusters = "../data/semantic-clusters-ids/json/clusters-ids.json"
topicNums = ["03", "21", "22", "26", "42", "51", "57", "66", "68", "88"]
path_epoch = sys.argv[1]
representatives_all = {}

if os.path.exists(path_epoch):
    os.remove(path_epoch)

file_clusters = open(path_clusters, "r")
data = json.load(file_clusters)
for i in range(len(topicNums)):
    representatives = Set()
    clusters = data["topics"]["MB" + topicNums[i]]["clusters"]
    for j in range(len(clusters)):
        clusters[j] = [s.encode("utf-8") for s in clusters[j]]
        representatives.add(clusters[j][0])
    representatives_all[topicNums[i]] = representatives
    

file_epoch = open(path_epoch, "a")

for topicNum in representatives_all:
    file_qrels = open("../data/qrels-microblog-epoch.txt", "r")
    lines = file_qrels.readlines()
    for line in lines:
        line = line.strip().split()
        if line[0] == "MB" + topicNum and int(line[3]) > 0:
            if line[2] in representatives_all[topicNum]:
                file_epoch.write(line[0] + " " + line[1] + " " + line[2] + " 2 " + line[4] + " " + line[5] + "\n")
            else:
                file_epoch.write(line[0] + " " + line[1] + " " + line[2] + " 1 " + line[4] + " " + line[5] + "\n")
file_qrels.close()
file_epoch.close()