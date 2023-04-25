num = 1224
natural_divisors = []
i = 1
while True:
    if i == num/2:
        break
    if (num / i).is_integer():
        natural_divisors.append(i)

    i += 1

print(len(natural_divisors))
