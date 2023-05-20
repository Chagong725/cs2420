def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num2 - num1

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num2 / num1

def int_to_string(num):
    return str(num)

def main():
    num1 = 2
    num2 = 3
    print("The sum of", num1, "and", num2, "is:", add(num1, num2))
    print("The difference of", num2, "and", num1, "is:", subtract(num1, num2))
    print("The product of", num1, "and", num2, "is:", multiply(num1, num2))
    print("The quotient of", num2, "divided by", num1, "is:", divide(num1, num2))
    num3 = 5
    num4 = 8
    print("The string representation of", num3, "is:", int_to_string(num3))
    print("The string representation of", num4, "is:", int_to_string(num4))

main()
