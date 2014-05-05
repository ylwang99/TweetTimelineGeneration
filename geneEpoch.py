from sets import Set
file = open("representatives/98.Australian floods.txt")
dt = Set()
lines = file.readlines()
for line in lines:
    line = line.strip().split()
    dt.add(line[0])
file.close()
file = open("data/qrels.microblog.epoch-rel.txt")
file_to = open("data/epoch.txt","a")
lines = file.readlines()
for line in lines:
    line = line.strip().split()
    if line[0] == "MB98" and int(line[3]) > 0:
        if line[2] in dt:
            file_to.write(line[0] + " " + line[1] + " " + line[2] + " 2 " + line[4] + " " + line[5] + "\n")
        else:
            file_to.write(line[0] + " " + line[1] + " " + line[2] + " 1 " + line[4] + " " + line[5] + "\n")
file_to.close()       
file.close()