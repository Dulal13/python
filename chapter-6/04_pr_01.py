def sum_minimums(lst):

    sum = 0
    for item in lst:
        sum += min(item)
    return sum

a = sum_minimums([
  [1, 2, 3, 4, 5],
  [5, 6, 7, 8, 9],
  [20, 21, 34, 56, 100]
])

print(a)

