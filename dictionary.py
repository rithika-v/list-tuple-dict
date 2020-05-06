mydict={"c":"Easy","C++":"Moderate","Java":"Tough"}
print(mydict)
print(len(mydict))
print(mydict["Java"])
print(mydict.get("c"))
mydict["Python"]="Cool"
print(mydict)
del mydict["c"]
print(mydict)
mydict["c"]="Easy"
print(mydict)
mydict.pop("c")
print(mydict)
mydict.clear()
print(mydict)
