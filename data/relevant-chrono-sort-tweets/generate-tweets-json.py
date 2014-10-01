topicsFile = "/Users/ylwang/Desktop/Temp/TTG evaluation/data/2014topics.txt"
dict = {}
topics = open(topicsFile, "r")
lines = topics.readlines()
for line in lines:
	line = line.strip().split("\t")
	dict[line[0]] = line[1]
topics.close()

for key in dict:
	topicNum = key
	topic = dict[key]
	file = open('txt/MB' + topicNum + '.txt', 'r')
	file_json = open('json/tweet_topic' + topicNum + '.json', 'a')
	file_json.write('{"topicid": "MB' + topicNum + '",\n"topic": "' + topic + '",\n"tweets":[\n')
	lines = file.readlines()
	count = 1
	for line in lines:
	    line = line.strip().split("\t")
	    if count == 1:
	    	file_json.write('{"id":"' + line[0] + '","time":"' + line[1] + '","name":"' + line[2] + '","screenname":"' + line[3] + '","text":"' + line[4].replace('"', "'") + '"}')
	    	count = count + 1
	    else:
	    	file_json.write(',\n{"id":"' + line[0] + '","time":"' + line[1] + '","name":"' + line[2] + '","screenname":"' + line[3] + '","text":"' + line[4].replace('"', "'") + '"}')
	file_json.write('\n]}')
	file.close()
	file_json.close()