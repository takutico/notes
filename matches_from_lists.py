# compare two lists in python and return matches



l1 = [0, 1, 2, 3, 4, 5, 69, 7, 8, 9]
l2 = [11, 22, 3, 44, 55, 6, 77, 8, 99, 0]

# in this example result should be 
# [3, 8, 0]
result = []
for i,j in zip(l1, l2):
	if j in l1:
		result.append(j)
	if i in l2:
		result.append(i)
print(list(set(result)))

'''
def get_match(l1, l2):
	for i,j in zip(l1, l2):
		if j in l1:
			yield j
		if i in l2:
			yield i

for i in get_match(l1, l2):
	print(list(set(i)))
'''

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)