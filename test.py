"""
0
1
1
2
3
5
8
13
"""


def fibonacci(n):
	a, b = 0, 1
	for i in range(n):
		print(a)
		a, b = b, a + b 


fibonacci(10)
