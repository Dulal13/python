myDict = {
    "boi" : "Book" , 
    "kolom" : "Pen",
    "ghori" : "Clock"
}
print("Options are , " , list(myDict.keys()))
a = input("Enput your bangla word : ")
print("Bangla word is : " , myDict.get(a , "noneIs"))