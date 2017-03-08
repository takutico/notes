d = {'a': 1, 'd': 3, 'f': 4, 's': 2}
# d = {'a': 1, 'd': 3, 'f': 4, 's': 2, 'x':99}

### OPTION 1
# if x exist in the dict return it if not None
'''
if 'x' in d:
	tmp = d['x']
else:
	tmp = 'Unknow'
'''

### OPTION 2
# if sentence in one line
# tmp = d['x'] if 'x' in d else 'Unknow'

### OPTION 3
# but we can use dict.get
tmp = d.get('x', 'Unknow')

print('x is {}'.format(tmp))