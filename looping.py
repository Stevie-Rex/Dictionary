dictionary = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

#for x in dictionary:
    #print(x)
    #print(dictionary[x])

for x, y in dictionary.items():
    print(f"key is: {x} value is {y}")