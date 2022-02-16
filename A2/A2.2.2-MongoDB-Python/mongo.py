#!/usr/bin/env python

from importlib.resources import path
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pymongo
import os

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
    mydict = {}
    pipeline = [
        {"$project": {"words": {"$regexFindAll": {"input": "$text", "regex": "(*UCP)\\b(han|hon|den|det|denna|denne|hen)\\b", "options": "i"}}}},
        {"$set": {"words": "$words.match"}},
        {"$unwind": {"path": "$words", "preserveNullAndEmptyArrays": False}},
        {"$group": {"_id": {"$toLower": "$words"}, "count": {"$sum": 1}}}
    ]
    result =mycol.aggregate(pipeline)
    # put the counting result into dictionary
    for i in result: 
        mydict[i["_id"]] = i["count"]
    mydict["unique tweets"] = mycol.count_documents({})
    mydict1 = {'hen': 34419, 'det': 532906, 'den': 1324057, 'han': 778945, 'denne': 4015, 'hon': 363764, 'denna': 22716, 'unique tweets': 2341577}
    print(mydict1)
    return mydict

def draw_data(mycol, mydict):
    unique_value = mycol.count_documents({})
    mydict = {'den': 1324057, 'denna': 22716, 'denne': 4015, 'det': 532906, 'han': 778945, 'hen': 34419, 'hon': 363764}
    for x in pronouns:
        mydict[x] = mydict[x] / unique_value
    df = pd.DataFrame({"pronouns":list(mydict.keys()), "normalized number":list(mydict.values())})
    sns.barplot(x="normalized number", y="pronouns", data=df)
    plt.show()

if __name__ == "__main__":
    # connect to MongoDB
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    dblist = myclient.list_database_names()
    mydb = myclient["tweets"]
    mycol = mydb["tweet"]
    #load_data(mycol)
    #delete_data(mycol)
    a = count_data(mycol)
    draw_data(mycol, a)
