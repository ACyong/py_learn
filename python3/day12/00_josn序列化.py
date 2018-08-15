import json

info = {
    'name': '庄AC',
    'age': 22
}
f = open('text.txt', 'w')
print(json.dumps(info))
json.dump(info, f)
# f.write(json.dumps(info))
# f.write(str(info))

f.close()
