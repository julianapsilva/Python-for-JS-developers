FRIENDS = [
    {"name": "Graham"},
    {"name": "John"},
    {"name": "Terry"},
    {"name": "Eric"},
    {"name": "Michael"}
]

NAME_STRINGS = [friend["name"] for friend in FRIENDS]
NAME_WITH_H = [name for name in NAME_STRINGS if "h" in name]

print(NAME_STRINGS)
print(NAME_WITH_H)