myDictionary_1 = {"a":1,"b":2,"c":3,"d":4}

tmpDictionary = myDictionary_1.copy()
print(tmpDictionary)

myDictionary_1["a"] = 10
print(myDictionary_1)

print(myDictionary_1.get("a"))