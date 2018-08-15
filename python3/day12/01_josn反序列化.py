import json

f = open('text.txt', 'r')
# data = eval(f.read())
# data = json.loads(f.read())
data = json.load(f)

f.close()

print(data['name'])
