import random
random_set = []

size = int(input("Enter the number of elements you want: "))
rng = int(input("Enter the start of the range: "))
rng2 = int(input("Enter the end: "))

for i in range(size):
	n = random.randint(rng, rng2)
	while n in random_set:
		n = random.randint(rng, rng2)
	random_set.append(n)

with open('numbers.txt', 'w') as f:
	f.write(str(len(random_set)))
	f.write('\n')
	for line in random_set:
		f.write(str(line))
		f.write('\n')