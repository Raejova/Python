def palindrome(mot):
    temp_list = list(mot)
    temp_list.reverse()
    if(''.join(temp_list) == mot):
        return(print("Le mot est un palindrome"))
    else:
        return(print("Le mot n'est pas un palindrome"))

palindrome(mot="radar")