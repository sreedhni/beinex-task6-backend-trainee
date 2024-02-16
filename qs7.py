# Write a Python program to Delete a list of keys from a dictionary

def remove_keys(dictionary, keys_to_delete):
    for key in keys_to_delete:
        if key in dictionary:
            del dictionary[key]
        else:
            print(f"Key '{key}' not found in the dictionary.")

dic={}
length = int(input("enter the length of the dictionary : "))
for i in range(length):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dic[key] = value
keys_input = input("Enter keys to delete (separated by spaces): ")
keys_to_delete = keys_input.split()
remove_keys(dic, keys_to_delete)

print("Dictionary after deleting keys:",dic)
