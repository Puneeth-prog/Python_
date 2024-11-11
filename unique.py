
print("enter a string ")
myStr=input()
print("The input string is:",myStr)
output=[]
for character in myStr:
    if character not in output:
        output.append(character)
print("The output is:",output)