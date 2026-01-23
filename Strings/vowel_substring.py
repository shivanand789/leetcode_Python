#Given a string, find the word with the highest number of vowels and return the sentence from the start up to that word.

def rearrange_target_word(sentence, target):
    words = sentence.split()

    if target in words:
        # 1. Remove the word from its current position
        words.remove(target)

        # 2. Split the word into two parts
        # "shiv" is first 4 chars, "anand" is the rest
        part1 = target[:4]
        part2 = target[4:]

        # 3. Rebuild the sentence
        middle = " ".join(words)
        return f"{part1} {middle} {part2}"

    return sentence


# Test
str2 = "my name is shivanand and i live in bangalore"
print(f"Rearrange Result: {rearrange_target_word(str2, 'shivanand')}")
# Output: shiv my name is and i live in bangalore anand