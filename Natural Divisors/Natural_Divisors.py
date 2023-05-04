num = int(input("Enter the number: "))
natural_divisors = []
i = 1
while True:
    if i == num/2:
        break
    if (num / i).is_integer():
        natural_divisors.append(i)

    i += 1

print(natural_divisors)
