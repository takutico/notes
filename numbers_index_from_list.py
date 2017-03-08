# get the index and number in a dictionary
l = ['asfd', '1', '44','g', '4 5', '7k', '563']
print({i:v for i, v in enumerate(l) if v.isdigit()})
