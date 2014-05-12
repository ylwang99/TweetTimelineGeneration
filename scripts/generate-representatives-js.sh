# This file is to:
# 1. extract representative of each semantic cluster per topic from /data/semantic-clusters/ to data/timeline-representatives/
# 2. generate corresponding epoch files into epoch.txt file
# 3. convert epoch.txt into js file so that it can be fed into timeline visualization

python helper-generate-representatives-txt.py
echo "representatives extraction done..."
python helper-generate-cluster-epoch.py epoch.txt
echo "epoch done..."
./helper-convert-epoch-to-js.pl ../data/topics-microblog-querytweet-epoch.txt epoch.txt > ../data/timeline-representatives/representatives.js
rm epoch.txt
echo "js done..."