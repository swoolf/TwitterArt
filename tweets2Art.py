import json
import pandas as pd
import re
from PIL import Image, ImageDraw
#import matplotlib.pyplot as plt

def word_in_text(word, text):
    if text:
        word = word.lower()
        text = text.lower()
        match = re.search(word, text)
        if match:
            return True
    return False

tweets_data_path = 'tweets8_16_2.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print len(tweets_data)
#print tweets_data[1]
tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet.get('text', None),tweets_data)
#tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

#print tweets['text'][47]

drawArray=[]
i=0
for tweet in tweets['text']:
    #print i
    i=i+1
    if word_in_text('north',tweet):
        drawArray.append('n')
    elif word_in_text('east',tweet):
        drawArray.append('e')
    elif word_in_text('south',tweet):
        drawArray.append('s')
    elif word_in_text('west',tweet):
        drawArray.append('w')
    elif word_in_text('red',tweet):
        drawArray.append('red')
    elif word_in_text('blue',tweet):
        drawArray.append('blue')
    elif word_in_text('green',tweet):
        drawArray.append('green')

width=4000
height=4000
im = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(im)

color='red'
x=width/2
y=height/2

m=10
r=6
for item in drawArray:
    if item == 'n':
        y=y+m
        if y>height:
            y=0;
    elif item =='e':
        x=x+m
        if x>width:
            x=0;
    elif item =='s':
        y=y-m
        if y<0:
            y=height
    elif item =='w':
        x=x-m
        if x<0:
            x=width;
    elif item =='red':
        color='red'
    elif item =='blue':
        color = 'blue'
    elif item =='green':
        color='green'
    draw.ellipse((x-r, y-r, x+r, y+r), fill=color)

im.save('try3.jpg')

