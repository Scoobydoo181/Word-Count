"""Counts and ranks the most common words in literary classics"""

import time
import re
import json

def update_json(results_dict):
    """Adds the input dictionary to a json file"""
    try:
        with open("cache.json",'w',encoding='UTF-8') as file:
            json.dump(results_dict,file)
    except IOError:
        pass

def reorder_and_sort(input_dict):
    """Reorders the input dictionary as a list of tulples and sorts it in decreasing order"""
    unsorted_results = ((value, key) for (key,value) in input_dict.items())
    return sorted(unsorted_results,reverse=True)

def count_words(file_names):
    word_counts = {}
    for file_name in file_names:    
        try:
            with open(file_name, encoding='UTF-8') as file:
                contents = file.read()
        except IOError:
            print('Error opening file')
            continue
        else:
            word_list = set(contents.split())
     
        for word in word_list:
            number_appearances = contents.count(word)

            formatted_word =  re.sub("[^a-zA-Z0-9']", '', word.lower())

            if formatted_word in word_counts.keys():
                word_counts[formatted_word] += number_appearances
            else:
                word_counts[formatted_word] = number_appearances
    return word_counts

start_time = time.time()

file_names = ['Books/a_modest_proposal.txt','Books/a_tale_of_two_cities.txt',
            'Books/dracula.txt','Books/frankenstein.txt','Books/heart_of_darkness.txt',
            'Books/little_women.txt','Books/moby_dick.txt','Books/oliver_twist.txt',
            'Books/pride_and_prejudice.txt','Books/the_scarlet_letter.txt','Books/ulysses.txt']
 
word_counts = count_words(file_names)

sorted_results = reorder_and_sort(word_counts)

update_json(sorted_results)

end_time = time.time()

elapsed_time = end_time-start_time
print("%s seconds" % str(elapsed_time))