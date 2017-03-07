def square(num_list):
	for i in num_list:
		yield(i * i)

for n in square([1,2,3,4,5,6,7,8,9]):
	print(n)
