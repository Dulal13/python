def pyramid_lists(n):
    
    lst = []
    for item in range(1 , n+1):
        l  = item*[item]
        lst.append(l)
    return lst



a = pyramid_lists(3)
print(a)

