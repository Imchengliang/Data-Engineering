import sys
import json
import re

pronouns = ["han", "hon", "den", "det", "denna", "denne", "hen", "unique_tweet"]

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if len(line) != 0:
        # use json to load the tweets
        jsonData = json.loads(line)
        # determine whether it's retweet or not
        if 'retweeted_status' not in jsonData:
            tweets = jsonData['text']
            # split the line into words
            pattern = re.compile(r"\w+")
            words = list(map(str, pattern.findall(tweets)))
            # increase counters
            words.append('unique_tweet')
            for word in words:
                word = word.lower()
                if word in pronouns:
                # write the results to STDOUT (standard output);
                # what we output here will be the input for the
                # Reduce step, i.e. the input for reducer.py
                #
                # tab-delimited; the trivial word count is 1
                    print(word, 1)
