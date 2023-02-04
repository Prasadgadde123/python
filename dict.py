dicttext = {
    "id":15,
    "name" : "gdv",
    "age" : "20"
}
print(dicttext.values())
dicttext["color"] = "white"
del dicttext["color"]
print(dicttext)
for x in dicttext:
    print(dicttext)
mydict = dicttext.copy()
print(mydict) 

