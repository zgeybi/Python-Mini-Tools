myList = []
numberOfTerms = int(input("Enter number of terms to be calculated: "))
orderOfElement = int(input("Enter the order of the element you want to check: "))
firstElement = int(input("Enter first element of the sequence: "))
secondElement = int(input("Enter second element: "))
myList.append(firstElement)
myList.append(secondElement)

for i in range(2, numberOfTerms):
    myList.append(((myList[i - 1] * 123) + (myList[i - 2] * 45)) % 10**9 + 4321)

with open("sequence.txt", 'w') as f:
    for line in myList:
        f.write(line)
        f.write('\n')

    myList.sort()
    f.write(str(myList[orderOfElement]))
