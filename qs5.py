# Write a Python program to multiply all the items in a dictionary. 
dic = {}
length = int(input("Enter the length of the dictionary: "))

for i in range(length):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dic[key] = value

multiply = int(input("Enter a value to multiply: "))
for key in dic:
    dic[key] *= multiply

print("Dictionary after multiplying all items:", dic)
