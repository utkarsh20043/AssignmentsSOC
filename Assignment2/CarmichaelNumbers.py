def carmichael_numbers(N):
    carmichael_numbers = []
    for i in range(2, N+1):
        if all([pow(a, i-1, i) == 1 for a in range(2, i)]):
                if all([(i-1) % (p-1) == 0 for p in prime_divisors(i)]):
                    carmichael_numbers.append(i)
    return carmichael_numbers

N = int(input("Enter a positive integer N: "))
print(carmichael_numbers(N))