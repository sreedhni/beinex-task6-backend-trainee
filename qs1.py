# Write a Python program to merge two Python dictionaries.


dict1 = {}
length1 = int(input("Enter the length of dictionary1: "))
for i in range(length1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

dict2 = {}
length2 = int(input("Enter the length of dictionary2: "))
for j in range(length2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

merged_dict = dict1.copy()  

for key in dict2:
    if key in dict1:
        print(f"Key '{key}' already exists in dictionary1.")
        choice = input(f"Which value do you want to keep? (old/new): ")
        if choice.lower() == 'new':
            merged_dict[key] = dict2[key]  
    else:
        merged_dict[key] = dict2[key]  

print("Merged dictionary:", merged_dict)
