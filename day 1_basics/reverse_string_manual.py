def reverse_string_manual(text):
    # handle empty or non-string inputs
    if not text or not isinstance(text,str):
        return text
    char_list=[]

    #Iterate from last index to 0
    for i in range(len(text)-1,-1,-1):
        char_list.append(text[i])

    return "".join(char_list)

input_string="my name is shiva"
print(f"original:{input_string}|Reversed:{reverse_string_manual(input_string)}")