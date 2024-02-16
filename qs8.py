# Create a function that takes a string and returns a dictionary where keys are letters, and values are the
#  number of times each letter appears in the string  
    
def letters_count(string):
    dic = {}
    for letter in string:
        if letter.isalpha(): 
            letter=letter.lower()
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
    return dic

given_string= input("Enter the string value: ")
result = letters_count(given_string)
if result:
    print("Letter counts:", result)
else:
    print("The given string doesnt contain any alphabets")

