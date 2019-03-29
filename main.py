import json
import os

from results_graph import make_graph
import word_count


path = os.path.dirname(__file__)
path = os.path.join(path, 'cache.json')

try:
    with open(path) as file:
        rankings = json.load(file)

except FileNotFoundError:
    word_count.get_data()
else:
    make_graph(rankings)
    
