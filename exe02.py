FRIENDS = [
    {"name": "Graham"},
    {"name": "John"},
    {"name": "Eric"},
    {"name": "Terry"},
    {"name": "Michael"}
]

for friend in FRIENDS:
    if "a" in friend["name"]:
        print(f"Hey {friend['name']}!")
