people = {}

people["Ayaz"] = 16
people["Ali"] = 21
people["Alex"] = 9

del people["Alex"]

print(people)

for key, value in people.items():
    print(f"{key}:{value}")