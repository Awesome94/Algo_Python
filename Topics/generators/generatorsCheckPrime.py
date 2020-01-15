def check_prime(number):
    for divisor in range(2, int(number*0.5)+1):
        if number % divisor == 0:
            return False
    return True

prime = (i for i in range(2, 1000) if check_prime(i))
print(prime)
for x in prime:
    print(x)

for z in prime:
    print("this is Z", z)