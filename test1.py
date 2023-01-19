print("hello world\n")
print("this is a practice.\n")
print("calculate the davinchi numbers:")

n1 = int(input("Please enter first number:"))
n2 = int(input("please enter the secend number:"))

x = int(input("please enter the number of calculated numbers:"))


for i in range(x):
    if i == 0:
        print(n1)
        print(n2)
    else:
        n1 , n2 = n2 , n1+n2
        print(n2)

print("\ncalculations are completed.")