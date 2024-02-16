# Write a Python program to get dictionary keys as a list 

dic = {}
try:
    length = int(input("Enter the length of the dictionary: "))
    for i in range(length):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dic[key] = value

    keys = list(dic.keys())
    print("List of dictionary keys:", keys)
except ValueError:
    print("Please enter an integer value for the length of the dictionary.")


