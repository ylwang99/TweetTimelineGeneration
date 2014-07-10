#This file is to take run file (as an input argument) and ground truth non-redundant tweets 
#to compute the weighted precision, recall and f1 score per topic.
import sys
import json
from sets import Set

#Take qrels to generate dictionary of {topic number:{tweetid:weight}} 
#where weight is 0(non-relevant), 1(relevant), 2(highly relevant)
qrels_dt = {}
file_qrels = open("../data/qrels-microblog-epoch.txt", "r")
lines = file_qrels.readlines()
for line in lines:
    line = line.strip().split()
    topic_ind = line[0][line[0].index("MB") + 2:]
    if topic_ind not in qrels_dt:
        qrels_dt[topic_ind] = {}
    qrels_dt[topic_ind][line[2]] = line[3]

#Take run file and generate dictionary of {topic number:Set of tweetids for that topic} 
clusters_run_dt = {}
file_run = open(sys.argv[1], "r")
lines = file_run.readlines()
for line in lines:
    line = line.strip().split()
    topic_ind = line[0][line[0].index("MB") + 2:]
    if topic_ind not in clusters_run_dt:
        clusters_run_dt[topic_ind] = Set()
    clusters_run_dt[topic_ind].add(line[2])

#Take ground truth, generate dictionary of {topic number:2D array of clusters of tweetids}, for each topic,
#calculate the total weights, the weight for each cluster,compare tweet from each cluster with that from
#run file and compute weighted precision, recall and f1 score.
clusters_dt = {}
precision_total = 0
recall_total = 0
f1_score_total = 0  
clusters_path = "../data/semantic-clusters-ids/json/clusters-ids.json"
file_clusters = open(clusters_path, "r")
data = json.load(file_clusters)
topics = data["topics"]
for topic in sorted(topics.keys()):
    total_weight = 0
    credits = 0
    topic_ind = topic[line[0].index("MB") + 2:]
    topic_ind = topic_ind.encode("utf-8")
    denominator_precision = len(clusters_run_dt[topic_ind])
    clusters_json = topics[topic]["clusters"]
    for i in range(len(clusters_json)):
        clusters_json[i] = [s.encode("utf-8") for s in clusters_json[i]]
    clusters_dt[topic_ind] = clusters_json
    for cluster in clusters_dt[topic_ind]:
        weight = 0
        hit_flag = 0
        for tweet in cluster:
            weight = weight + int(qrels_dt[topic_ind][tweet])
            if tweet in clusters_run_dt[topic_ind]:
                hit_flag = 1
        total_weight = total_weight + weight
        if hit_flag == 1:
            credits = credits + weight
            denominator_precision = denominator_precision + weight - 1
            hit_flag = 0
    print "MB" + str(topic_ind)
    precision = float(credits) / denominator_precision
    recall = float(credits) / total_weight
    if precision == 0 and recall == 0:
        f1_score = 0.0
    else:
        f1_score = 2 * precision * recall / (precision + recall)
    precision_total = precision_total + precision
    recall_total = recall_total + recall
    f1_score_total = f1_score_total + f1_score
    print "Precision\t\t" + str(precision)
    print "Recall\t\t\t" + str(recall)
    print "F1 score\t\t" + str(f1_score)
precision_mean = precision_total / len(clusters_dt)
recall_mean = recall_total / len(clusters_dt)
f1_score_mean = f1_score_total / len(clusters_dt)
print "All"
print "Average precision\t" + str(precision_mean)
print "Average recall\t\t" + str(recall_mean)
print "Average f1 score\t" + str(f1_score_mean)
file_qrels.close()
file_run.close()
file_clusters.close()