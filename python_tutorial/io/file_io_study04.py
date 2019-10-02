import json

j_data = json.dumps([1, 'simple', 'list'])
print(type(j_data), j_data)

with open('json_test.txt', 'w', encoding='utf-8') as f:
    json.dump(j_data, f)


with open('json_test.txt', 'r', encoding='utf-8') as f:
    x = json.load(f)
    print(type(x), x)
