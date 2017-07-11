def read_file(file):
	with open(file) as f:
		for line in f:
			for w in word_list:
				word_count[w] = word_count[w] + 1 if w in word_count else 1
			yield line

for i in read_file('most_frecuent_words.txt'):
	print(i)
