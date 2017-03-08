def brackets(A):
	stack = []
	opener = ['{', '[', '(']
	closer = ['}', ']', ')']
	bracket_list = dict(zip(closer, opener))

	# first we can check if A start with closer
	if A and (A[0] in closer or A[-1] in opener):
		return 0

	for i in A:
		if i in opener:
			stack.append(i)
		elif i in closer:
			if stack and bracket_list[i] == stack[-1]:
				del stack[-1]
		# print(stack)

	return 0 if stack else 1

print(brackets('(()(())())'))  # True
print(brackets('{[()()]}'))  # True
print(brackets('([)()]'))  # False
print(brackets('}()]'))  # False