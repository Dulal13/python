myStory = {
        'name' : 'Md.Dulal Miah',
        'job'  : 'web developer',
        'marks' : [1,2,6],
        'anotherDict' : {'goal' : 'Jannat'}
}
# Two ways to get dictionary item

# print(myStory.get('name'))
# print(myStory['job'])
# print(myStory['marks'][2])

print(myStory['anotherDict']['goal'])

# this is unordered , mutable

myStory['marks'] = [4,5,78]
print(myStory)
