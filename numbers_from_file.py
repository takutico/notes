
# f = open('test.txt')

# print[line for line in f if line.isdigit()]

# for line in f:
# 	if line.strip('\n').isdigit():
# 		print(line.strip('\n'))
# f.close()

with open('numbers_from_file.txt') as f:
	print[line.strip('\n') for line in f if line.strip('\n').isdigit()]
