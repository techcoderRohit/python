#creating a dictionary

data = { "name": "Jake", "age": 22 }
print(data)

a = {"x": 1, "y": 2}
print(a)

b = dict(name="Sam", age=20)
print(b)

#accessing dictionary items

d = {"name": "Kat", "age": 21}

print(d["name"])     # Access using key
print(d.get("age"))  # Access using get()

#adding and updating dictionary items

d = {"name": "Sam"}

d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)

#removing dictionary items - del,pop,popitem and clear

d = {"a": 1, "b": 2}
del d["a"]
print(d)

d = {"a": 1, "b": 2}

val = d.pop("a")
print(val)
print(d)

d = {"a": 1, "b": 2}
print(d.popitem())

d = {"a": 1, "b": 2}
d.clear()
print(d)

#iterating through a dictionary

#iterate keys
d = {"a": 1, "b": 2}
for key in d:
    print(key)

#iterate values
d = {"a": 1, "b": 2}
for value in d.values():
    print(value)

#iterate key-value pairs
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)

#nested dictionaries

d = {
    "student": {
        "name": "Sam",
        "age": 20
    }
}

print(d["student"]["name"])