# python file for scrapping twitter image links from from @samdoesarts

import snscrape.modules.twitter as sntwitter
import itertools
import ree
import sys

tweet_list=[]
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:samdoesarts').get_items()):
    if i>int(sys.argv[1]):
        break
    tweet_list.append(tweet.media)

#print(tweet_list)
small=[]

for i in tweet_list:
    try:
        small.append(re.findall("fullUrl=(.*large')",str(i[0]))[0])
    except:
        pass

with open("imgLink", "w") as f:
    for i in small:
        f.write(f"{i} \n")
