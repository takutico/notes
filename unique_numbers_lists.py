# find unique numbers from 2 lists

l1 = [0, 1, 2, 3, 4, 5, 6, 69, 7, 8, 9, 'l']
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 99, 9, 'p']

# l1 = list(set(l1))
# l2 = list(set(l2))

print(list(set(l1) - set(l2)) +list(set(l2) - set(l1)))


# print(list(set(l1 + l2)) +list(set(l2) - set(l1)))

print(list(set(l1)^set(l2)))

