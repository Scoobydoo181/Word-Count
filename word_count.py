"""Counts and ranks the most common words in literary classics"""
import numpy
from collections import OrderedDict
import time
import re
start_time = time.time()
file_names = ['Books/a_modest_proposal.txt','Books/a_tale_of_two_cities.txt',
            'Books/dracula.txt','Books/frankenstein.txt','Books/heart_of_darkness.txt',
            'Books/little_women.txt','Books/moby_dick.txt','Books/oliver_twist.txt',
            'Books/pride_and_prejudice.txt','Books/the_scarlet_letter.txt','Books/ulysses.txt']

word_counts = OrderedDict()            
for file_name in file_names:    
    try:
        with open(file_name, encoding='UTF-8') as file:
            contents = file.read()
            word_list = set(contents.split())

            for word in word_list:
                number_appearances = contents.count(word)
                
                if re.sub('[^a-zA-Z0-9 \n]', '', word.lower()) in word_counts.keys():
                    word_counts[re.sub('[^a-zA-Z0-9 \n]', '', word.lower())] += number_appearances
                else:
                    word_counts[re.sub('[^a-zA-Z0-9 \n]', '', word.lower())] = number_appearances
    except IOError:
        print('Error opening file')
        continue
	
sorted_dict = sorted(((key, value) for (key,value) in word_counts.items()),reverse=True)

try:
    with open("results.txt",'w',encoding='UTF-8') as file:
        file.write(str(sorted_dict))
except IOError:
    pass
end_time = time.time()

print("%s seconds" % str(float(end_time)-float(start_time)))