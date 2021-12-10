import json
import os.path

with open(r"mainapp/json_products/product.json", "r", encoding="utf-8") as jsonfile:
    data = json.load(jsonfile)

print(type(data))
print(data)

print(os.path.dirname(__file__))
print(__file__)

test_dict = {
    "один": 1,
    "два": 2,
    "три": 3,
}

print(test_dict)
print(len(test_dict.keys()))

for key, val in test_dict.items():
    print(key, val)