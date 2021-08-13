def keyboard_mistakes(txt):
    txt = list(txt)
    myDict = {
        "4":"A",
        "5":"S",
        "0":"O",
        "1":"I"
    }
    item = ["4","5","0","1"]
    s = ''
    for i in range(0,len(txt)):
      if txt[i] in item:
          txt[i] = myDict.get(txt[i])
    for char in txt:
        s += char
    return s
        
a = keyboard_mistakes("51NG4P0RE")
print(a)