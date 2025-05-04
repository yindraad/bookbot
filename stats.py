def get_num_words(text):
    words = text.split()
    return len(words)

def string_to_character(text):
    char_count = {} 
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sorted_char_count(char_count):
    return dict(sorted(char_count.items()))