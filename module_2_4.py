# Всё не так уж просто.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i > 2:
        for j in range(2, i):
            if i % j != 0:
                is_prime = False
            else:
                is_prime = True
            if is_prime = True:
                primes.append(i)
            else:
                not_primes.append(i)
    elif i = 2:
        

    else:
        continue
print(primes)
print(not_primes)






        # if i > 1 and i % 1 == 0 and i % j == 0:
        #     is_prime = True
        # elif i > 1:
        #     is_prime = False
        # else:
        #     continue
        # if is_prime == True:
        #     print(f'простое число = {i,j}')
        # else:
        #     print(f'Не простое число {i,j}')