import os
import time

i = 1

queries = []
with open("google_queries_short.txt", "r") as f:
    for line in f.readlines():
        queries.append(line.rstrip('\n'))

for q in queries:
    if not os.path.exists("./google_csv/q{}.csv".format(i)):
        os.system('pop8query --gscholar --keywords=\'{}\' "./google_csv/q{}.csv"'.format(q, i))
    else: 
        print("File q{}.csv already exists.".format(i))
    i+=1
    time.sleep(5)