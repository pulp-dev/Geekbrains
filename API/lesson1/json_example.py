import json
from pprint import pprint


def write_json(d: dict, filename: str) -> None:
    with open(filename, "w") as f:
        json.dump(d, f, indent=2)
        # json.dumps - строкой


def read_json(filename):
    with open(filename, 'r') as f:
        d = json.load(f)
        # json.loads - читать строку
    return d


d = {
    "fruits": ["apple",
               "banana",
               ],
    "price": 139.9,
}

filename = 'fruits.json'
write_json(d, filename)
print(read_json(filename))
print()
