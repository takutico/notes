# having a list of [type, START/STOP, time]
l = [
    ['Get_foo', 'START', '0'],
    ['Get_foo', 'STOP', '50'],
    ['Get_foo', 'START', '20'],
    ['Get_back', 'START', '30'],
    ['Get_foo', 'STOP', '30'],
    ['Get_back', 'STOP', '0'],
    ['Get_foo', 'START', '50'],
    ['Get_foo', 'STOP', '60']
]

# get the average group by type
data = {}
result = {}
for i in l:
    if i[0] not in data:
        data[i[0]] = int(i[2])
    else:
        result[i[0]] = (data[i[0]] + int(i[2])) / 2

print(result)
