# i = 0
# while i<10:
#     print(i , 'Md.Dulal Miah')
#     i = i + 1
def greeting(name):
    if name == "Mubashir":
        return "Hello, my Love!"
    else:
        return "Hello, {}!".format(name)

a = greeting("Helen")
print(a)