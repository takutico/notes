# fibonecci sequence
'''
a, b = 0, 1

for i in range(10):
	print(a)
	a, b = b, a + b
'''

# fibonacci generator
def fib(num):
	a, b = 0, 1
	for i in range(num):
		yield(a)
		a, b = b, a + b

for i in fib(10):
	print(i)