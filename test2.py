l = [3,'s','d',4,5,'r']
result = []

# print([ i for i in l if str(i).isdigit()])

with open('numbers_from_file.txt') as f:
	for l in f:
		if str(l.strip('\n')).isdigit():
			print(l)
