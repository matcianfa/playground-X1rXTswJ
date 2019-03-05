def est_palindrome(mot):
    if len(mot)<2: return True
    else:
        return mot[0]== mot[-1] and est_palindrome(mot[1:-1])
