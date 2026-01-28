def is_palindrome(text):
    """
    checks if a given input is an palindrome or not
    """
    # 1. Handle edge cases (empty strings or non-strings)
    if not isinstance(text,str):
        return False
    #2 Manual Reversal
    char_list=[]
    for i in range(len(text)-1,-1,-1):
        char_list.append(text[i])

    reversed_text="".join(char_list)

    return reversed_text==text
word="malayalam"
if is_palindrome(word):
    print(f"{word} is palindrome")
else:
    print(f"{word} is not a plaindrome")

