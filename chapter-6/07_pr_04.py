def invert(dct):
    key = list(dct.keys())
    value = list(dct.values())
    newDct = {}
    for i in range(0 , len(key)):
        newDct.update({value[i]:key[i]})
    return newDct


a = invert({ "z": "q", "w": "f" })
print(a)
