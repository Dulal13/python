def two_digit_sum(n):
    sum = 0
    while n!=0:
         rem = n%10
         sum += rem
         n = int(n/10)
    return sum

a = two_digit_sum(49)
print(a)

