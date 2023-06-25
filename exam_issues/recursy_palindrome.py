
def palindrome(word):
    n = len(word)
    if n <= 1:
        return True
    elif word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return False
    
print(palindrome('флдлф'))