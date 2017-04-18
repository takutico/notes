"""
Find the 10 most frecuent words in a text file
"""

import re

with open('most_frecuent_words.txt') as f:
	word_count = {}
	for line in f:
		# Use regular ex. to find only words and not symbols
		word_list = re.findall(r'\w+', line) 
		# word_list = line.lower().split()
		for w in word_list:
			word_count[w] = word_count[w] + 1 if w in word_count else 1

# word_count = sorted(word_count, key=word_count.get, reverse=True)
# but this will return a list and don't know the number of repetitions

# use lambda
word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

print(word_count[:5])
				