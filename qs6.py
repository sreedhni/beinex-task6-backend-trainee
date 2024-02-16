# Write a Python program to get the maximum and minimum values of a dictionary 

dic = {}
length = int(input("Enter the length of the dictionary: "))

for i in range(length):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dic[key] = value

numeric_values = [int(val) for val in dic.values() if val.isdigit()]

if numeric_values:
    max_value = max(numeric_values)
    min_value = min(numeric_values)
    print("Maximum value in the dictionary:", max_value)
    print("Minimum value in the dictionary:", min_value)
else:
    print("No numeric values found in the dictionary.")
