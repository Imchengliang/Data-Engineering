#!/usr/bin/env python

from importlib.resources import path
#import seaborn as sns
#import matplotlib.pyplot as plt
#import pandas as pd
import pymongo
import os
import json
import re

def load_data(mycol):
    path = "tweets"
    files = os.listdir(path)
    for fine in files:
        if not os.path.isdir(fine):
            f = open(path+"/"+fine)
            for line in f:
                line = line.strip()
                if len(line) != 0:
                    jsonData = json.loads(line)
                    if 'retweeted_status' not in jsonData:
                        x = mycol.insert_one(jsonData)
                        #print(x)
    return x

def delete_data(mycol):
    x = mycol.delete_many({})
    print('All data are deleted')
    return x

def count_data(mycol):
    pronouns = ["han", "hon", "den", "det", "denna", "denne", "hen"]
    mydict = dict(zip(pronouns, [i-i for i in range(7)]))
    for x in pronouns:
        for y in mycol.find({"text":{"$regex":x, "$options":"$i"}}):
            mydict[x] = mydict[x] + 1
    print(mydict, mycol.count_documents({}))
    return pronouns, mydict

def draw_data(mycol, pronouns, mydict):
    unique_value = mycol.count_documents({})
    for x in pronouns:
        mydict[x] = mydict[x] / unique_value
    df = pd.DataFrame({"pronouns":list(mydict.keys()), "normalized number":list(mydict.values())})
    sns.barplot(x="normalized number", y="pronouns", data=df)
    plt.show()
    #print(mydict)

    '''
    for x in mycol.find({}, { "text": 1 }):
        #x = json_util.dumps(x)
        tweet = x['text']
        pattern = re.compile(r"\w+")
        words = list(map(str, pattern.findall(tweet)))
        for word in words:
            word = word.lower()
            if word in pronouns:
                print(word, 1)
    '''

if __name__ == "__main__":
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    dblist = myclient.list_database_names()
    mydb = myclient["tweets"]
    mycol = mydb["tweet"]
    load_data(mycol)
    #delete_data(mycol)
    a, b = count_data(mycol)
    #draw_data(mycol, a, b)
