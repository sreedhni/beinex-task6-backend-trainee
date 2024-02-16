# Write a Python program to sum all the items in a dictionary.

dic = {}
sum = 0
length = int(input("Enter the length of the dictionary: "))

for i in range(length):
    key = input("Enter key: ")
    value = input("Enter value : ")
    dic[key] = value

    if value.isdigit():
        sum += int(value)
    else:
        print(f"Value '{value}' is not an integer and will be ignored.")

print("Sum of integer values in the dictionary:", sum)
