"""Show a graph of the results"""
from matplotlib import pyplot as plt
import json

file = open("cache.json")
rankings = json.load(file)
file.close()

words =  [(y) for (x,y) in rankings[:75]]
counts = [(x) for (x,y) in rankings[:75]]

plt.figure(figsize=(12,8))
plt.xticks(rotation=280)
plt.title('Most commonly used words in literature')
plt.ylabel('Number of Occurences')
plt.xlabel('Word')

plt.bar(words,counts)
plt.show()