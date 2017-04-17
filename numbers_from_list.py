L = ['asfd', '1', '44','g', '4 5', '7k', '563']

# tl =[]
# for i in l:
# 	if i.isdigit():
# 		tl.append(i)

# using for loop
print('Using loop')
print([i for i in L if i.isdigit()])

import re

print('Using regular expressions')
s = '123fdsf24rt3g4'
m = re.findall(r'\d+', s)
print(m)
# print(x for x in re.match(r'\d+', s))
