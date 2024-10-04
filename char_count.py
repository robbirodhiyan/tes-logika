import re

def count_words(sentence):
    words = sentence.split()
    
    valid_words = [word for word in words if re.match(r'^[a-zA-Z]+[,.!?;:]*$', word)]
    
    return len(valid_words)

sentence_input = input("Input: ")

output = count_words(sentence_input)

print(f"Output: {output}")
