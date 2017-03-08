# Bad way
'''
f = open('django.md')
text = f.read()
for line in text.split('\n'):
	print(line)
f.close()
'''

# better way
'''
f = open('django.md')
for line in f:
	print(line)
f.close()
'''

# best way
with open('django.md') as f:
	for line in f:
		print(f)