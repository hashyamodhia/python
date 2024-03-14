book = {}
book['tom'] = {
    'name' : "jkf",
    'address' : "45, street jfdl",
    'phone' : "897465485"
}
book['jack'] = {
    'name' : "asd",
    'address' : "89, street qwert",
    'phone' : "8745945689"
}

import json

s = json.dumps(book)
print(s)
t = type(s)
print(t)
p = book['tom']['phone']
print(p)

for person in book:
    print(book[person])