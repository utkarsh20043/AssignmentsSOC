def Sum_of_divisors(n):
    sum = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            sum = sum + i
    return sum

counter = 0

for j in range(1,100000):
    S = 0
    S = Sum_of_divisors(j)
    if j == S:
        continue
    if j == Sum_of_divisors(S) and j > S:
        print('pair : '+str(j)+' ' + str(S))
        counter = counter + 1
    if counter == 10:
        break
 