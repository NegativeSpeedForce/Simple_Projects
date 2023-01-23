#build a sum dunction with to input.

num1 = int(input("Enter first number:"))
num2 = int(input("Enter secend number:"))

def sum_numbers(first_number,second_number):
    
    sum_of_numbers = first_number + second_number
    return sum_of_numbers

print(sum_numbers(num1,num2))






#building function to sum up a list of data.

def sum_list(input_list):
    sum_of_list = 0
    for i in input_list:
        sum_of_list = sum_of_list + i
    return sum_of_list

star = [1,2,3,4,5,67,7,8,23456]
print(sum_list(star))






#make a operation to automaticaly get numbers and then using function sum_list() sum them up.

list_numbers = []

operation = input("please enter operation:")

if operation == "sum":
    while True:
        data = input("please enter number:")
        if data == "exit":
            break
        else:
            list_numbers.append(int(data))

print("this is the sum of number you entered:",sum_list(list_numbers))
