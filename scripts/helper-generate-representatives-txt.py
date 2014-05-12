# This file is to extract representative of each semantic cluster per topic from /data/semantic-clusters/ to data/timeline-representatives/

import os

path_clusters = "../data/semantic-clusters/txt/"
path_representatives = "../data/timeline-representatives/"

dirs = os.listdir(path_clusters)
for file in dirs:
    if file[-4:] == ".txt":
        file_clusters = open(path_clusters + file, "r")
        if os.path.exists(path_representatives + file):
            os.remove(path_representatives + file)
        file_representatives = open(path_representatives + file, "a")
        lines = file_clusters.readlines()
        representative = 1
        for line in lines:
            line = line.strip()
            if len(line) != 0:
                if representative == 1:
                    file_representatives.write(line + "\n")
                    representative = 0
            else:
                representative = 1
        file_clusters.close()
        file_representatives.close()