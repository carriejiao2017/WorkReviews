i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print("Numbers now:" , numbers)
    print("At the bottom i is %d" % i)

print("The numbers:")

for num in numbers:
    print (num)

number2 = []
for i in range(0,6):
    number2.append(i)

print(number2)