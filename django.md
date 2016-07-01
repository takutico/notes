# POST DATA
```python
# To retrieve the keys and values together, use the items method.
for key, value in request.POST.items():
    print(key, value)
# Note that request.POST can contain multiple items for each key.
# If you are expecting multiple items for each key, you can use lists, which returns all values as a list.
for key, values in request.POST.lists():
    print(key, values)
```
