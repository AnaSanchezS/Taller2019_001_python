# TestAutomatedAlarm.py

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

    
    #Importing the modules
import urllib2
import json

screen_name = "wordpress"

url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + screen_name

data = json.load(urllib2.urlopen(url))

print len(data), "tweets"

for tweet in data:
    print tweet['text']
