print("\nTask 1")
#  The user types in a string. Check if this string is a palindrome.
#  A palindrome is a word or text that reads the same backward as forward.
#  For instance, racecar; "Do geese see God?"; tenet; "Was it a car or a cat I saw?"

import re

# Acesta este un type hint, type hint-ul e ca o etichetă care spune “ce tip ar trebui să aibă parametrul și ce tip va returna funcția”.


def is_palindrome(
    text: str,
) -> bool:
    cleaned = re.sub(r"[A-Za-z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


yourstr = input("Enter a string to check if it is a polindrome: ")
yourstr2 = yourstr[::-1]

if is_palindrome(yourstr) is True:
    print(f"{yourstr} is a polindrome")
else:
    print(f"{yourstr2} isn't a polindrome")


print("\nTask 2")
#  The user types in text followed by a list of reserved words.
#  Find all reserved words in the text and change lowercase to uppercase there. Print the modified text.

import re


def highlight_reserved_words(text: str, reserved: list) -> str:
    words = text.split()
    reserved_lower = [r.lower() for r in reserved]
    result = []

    for word in words:
        stripped = re.sub(r"\W+", "", word)  # filterza semnele de punctuatie
        if stripped.lower() in reserved_lower:
            # verifica daca cuvintele din stripped sunt in reserved
            result.append(word.upper())
        else:
            result.append(word)

    return " ".join(result)


text = input("Please enter a string: ")
reserved = input("Enter the words you want highlighted: ").split()
print(highlight_reserved_words(text, reserved))


print("\nTask 3")
#  There is some text. Count the number of sentences in it and print the result.
import re


def sentence_counter(text: str) -> int:
    sentences = re.split(r"[.?!+]", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)


text = input("Enter some sentences to count them: ")
print(sentence_counter(text))
