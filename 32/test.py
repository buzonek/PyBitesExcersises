items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]


def duplicate_items(items):
    return items.copy()
    #return [x.copy() for x in items]

dupa = duplicate_items(items)

dupa[0]['name'] = 'maczek'

print(id(items[0]))
print(id(dupa[0]))