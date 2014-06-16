# This file is to:
# 1. generate corresponding epoch files into epoch.txt file
# 2. convert epoch.txt into js file so that it can be fed into timeline visualization

python helper-generate-cluster-epoch.py epoch.txt
echo "epoch done..."
./helper-convert-epoch-to-js.pl ../data/topics-microblog-querytweet-epoch.txt epoch.txt > ../data/representatives.js
rm epoch.txt
echo "js done..."