
# f = open('test.txt')

# print[line for line in f if line.isdigit()]

# for line in f:
# 	if line.strip('\n').isdigit():
# 		print(line.strip('\n'))
# f.close()


# Direct
with open('numbers_from_file.txt') as f:
	print[line.strip('\n') for line in f if line.strip('\n').isdigit()]


# Using generator
def reader():
	with open('numbers_from_file.txt') as f:
		for line in f:
			yield(line)


print[line.strip('\n') for line in reader() if line.strip('\n').isdigit()]
