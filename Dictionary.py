# this is the example of dictionary
# which is same as the list and it is mutable means modifiable
# it contains key for attribute value meand Abbas has a key Name
data ={"Name":"James","Age":30,"Country":"US"}
name=data["Name"]
age=data["Age"]
country=data["Country"]

print(name)
print(age)
print(country)

# another way to display key values
for key in data:
    print(data[key])
