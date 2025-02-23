def get_number_of_words(text):
    return len(text.split())

def get_character_counts(text):
    chars = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars

def sort_character_counts(chars):
    return dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))