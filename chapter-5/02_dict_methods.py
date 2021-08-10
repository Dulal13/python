myStory = {
        'name' : 'Md.Dulal Miah',
        'job'  : 'web developer',
        'marks' : [1,2,6],
        'anotherDict' : {'goal' : 'Jannat'}
}

# print(list(myStory.keys())) #prints the key of dic()
# print(list(myStory.values())) #prints the value of dic() as a list

print(myStory.items())

myWife = {
    'nameOfWife' : 'Tasli'
}

myStory.update(myWife)

print(myStory)