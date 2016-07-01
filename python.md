# LIST
```python
# The method max() returns the elements from the list with maximum value
# The method min() returns the elements from the list with minimum value.
my_string.split()  # already split with space
' '.join(['a','b','c'])  ## JOIN return 'abc'
```
# DICTIONARY
``` python
## LOOP with key and value
d={'e':'r', 't':'u', 'v':'m'}
for k, v in d.items():  # Note: d.items()
    print('%s %s' % (k, v))
## LOOP in one line
[i for i, x in enumerate(list_a) if x == j]
## REMOVE from dictionary
d.pop('key')
```
# COLLECTIONS
```python
## Counter
from collections import Counter
myList=[1,1,2,3,4,5,3,2,3,4,2,1,2,3]
Counter(myList)  # Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
Counter(myList).items()  # [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
Counter(myList).keys()  # [1, 2, 3, 4, 5]
Counter(myList).values()  # [3, 4, 4, 2, 1]
```
# STRING
```python
## Start With
'takuya'.startswith('ta')  # return True
```
# REGULAR EXPRESSION
```python
import re
print(bool(re.search(r'ly', 'ly should be in the beginning')))
print(bool(re.match(r'^[+-]?\d+\.\d+$', str(input()))))  # float string
# re.match() checks for a match only at the beginning of the string, while re.search() checks for a match anywhere in the string
```
# HTMLParser
```python
from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Found a start tag  :", tag)
    def handle_endtag(self, tag):
        print("Found an end tag   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Found an empty tag :", tag)
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head><body><h1>HackerRank</h1><br /></body></html>")
```
