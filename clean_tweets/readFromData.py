import sys
import re
import pprint
from cleanTweets import Tweet
#get the sentence and from a single line of the file
def getInfoFromLine(line):
    var = [m.start() for m in re.finditer('\t',line)]
    sen = line[var[0]+1:var[1]].strip()
    return sen

#lists to store tweets
tweets = []
with open(sys.argv[1],'r') as f:
    lines = f.readlines()

for line in lines[:50]:
    sen = Tweet(getInfoFromLine(line))
    tweets.append( {'original':sen.getTweet(orig=True), 'cleaned':sen.defaultClean()} )
    print(f'{lines.index(line)+1}/{len(lines)}')

with open('orig.txt','w') as orig, open('clean.txt','w') as clean:
    for tweet in tweets:
        orig.write(tweet['original']+'\n')
        clean.write(' '.join(tweet['cleaned'])+'\n')
