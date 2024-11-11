print("Enter a word to check if it is palindrome")
a=input()              # Take input from user
a=a.lower()            # change the string to lower case
b=a[::-1]              # String will be reversed and assigned to b
if a==b:               # comparing a and b string
    print(True)
else:
    print(False)