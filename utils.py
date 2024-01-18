import re
import unidecode


def remove_diacritics(text):
    return unidecode.unidecode(text)

def remove_punctuation(text):
    pattern = r'[^\w\s]'
    text_without_punctuation = re.sub(pattern, '', text)
    return text_without_punctuation



if __name__ == "__main__":
    print(remove_punctuation("Hello, how are you?!"))