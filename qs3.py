# Write a Python program to print a dictionary where the keys are numbers between 1 and 15 
# (both included) and the values are the square of the keys 

#1) 
# dic= {}
# for num in range(1, 16):
#     dic[num] = num ** 2
# print(dic)


# 2)
dic = {}
invalid_data = False
print("Enter numbers between 1 and 15 (separated by spaces):")
given_values = input()

if ' ' not in given_values:
    if given_values.isdigit():  
        num = int(given_values)
        if 1 <= num <= 15:
            dic[num] = num ** 2
        else:
            invalid_data = True
            print(f"The given input value {num} is out of range. Ensure the number is between 1 and 15")
    else:
        invalid_data = True
        print("Please enter a valid number between (1 and 15) and separate it by space .")
else:
    numbers = given_values.split()
    numbers = [int(num) for num in numbers]
    for num in numbers:
        if 1 <= num <= 15:
            dic[num] = num ** 2
        else:
            invalid_data = True
            print(f"The given input value {num} is out of range. Ensure the number is between 1 and 15")

if not invalid_data:
    print("Dictionary containing the squares of the user-selected numbers:",dic)
