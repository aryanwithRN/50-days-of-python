# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def panagrams(user_input:str)-> bool:
    check = "abcdefghijklmnopqrstuvwxyz"
    for i in check:
        if i not in user_input:
            return False
    return True
user_input = ("The quick brown fox jumps over the lazy dog").lower() 
# user_input = input("Enter a string: ").lower()
p = panagrams(user_input)
if p == True:
    print("Panagram ")
else:
    print("Not panagram")