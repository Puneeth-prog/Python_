# Python3 program for the above approach
from collections import Counter


# function to check if two strings are
# anagram or not
def check(s1, s2):
    # implementing counter function
    if (Counter(s1) == Counter(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


# driver code
print("enter first string")
print("enter second string")
s1 = input()
s2 = input()
check(s1, s2)
