def biger_number(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "numbers are equal."

n1 = int(input("please enter first number:"))
n2 = int(input("please enter second number:"))

print(biger_number(n1,n2))
