# Create a function that takes a string and returns a dictionary where keys are letters, and values are the
#  number of times each letter appears in the string  
    
def letters_count(string):
    dic = {}
    for char in string:
        if char == ' ':#this conition is used to skip counting the space between the words 
            continue
        elif char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic

input_string = input("Enter the string value: ")
result = letters_count(input_string)
print("Letter counts (excluding spaces):", result)

