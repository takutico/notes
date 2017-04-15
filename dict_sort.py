d = {'third': 3, 'second': 2, 'Fourth': 4, 'first': 1}

print(sorted(d, key=d.get))
# ['first', 'second', 'third', 'Fourth']

print(sorted(d, key=d.get, reverse=True))
# ['Fourth', 'third', 'second', 'first']

print(sorted(d.items(), key=lambda x:x[1]))
# [('first', 1), ('second', 2), ('third', 3), ('Fourth', 4)]

