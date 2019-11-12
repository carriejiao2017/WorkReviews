def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return(a + b)

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a,b))
    return(a - b)

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return(a * b)

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return(a / b)

print("Let`s do some math with just functions!")

age = add(30, 5)
heght = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, heght, weight, iq))

# A puzzle
print("Here is puzzle.")

what = int(add(age, subtract(heght, multiply(weight, divide(iq, 2)))))
print("That becomes:", what, "Can you do it by hand?")

def mul(a, b, c, d):
    print("fuction: %d + %d / %d - %d" % (a, b, c, d))
    return(a + b /c - d)

result = mul(1, 2, 3, 4)
print(result)