# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# else:
#     print("done")

def count_d(sentence):
    sentence = sentence.lower()
    return sentence.count('d')

a = count_d("My friend Dylan got distracted in school.") 
print(a)