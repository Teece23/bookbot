def get_num_words(text):
    words = text.split()
    return len(words)



def char_count(text):
    chars = {}
    for t in text:
        char = t.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] =1
    return chars

def dict_sort(chars):
    list_dict = [{"char": k, "count": v} for k, v in chars.items()]
    list_dict.sort(key=lambda item: item["count"], reverse=True)
    return list_dict

    
    