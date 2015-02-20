__author__ = 'Omar Quimbaya'

word_one = input("Enter the first word: ")
word_two = input("Enter the second word: ")


def is_anagram(string_one, string_two):
    stripped_string_one = string_one.strip()
    stripped_string_two = string_two.strip()

    if not stripped_string_one.isalpha() and not stripped_string_two.isalpha():
        print("Strings must be single words only. There also cannot be numbers in it.")
        return False

    sorted_string_one = sorted(stripped_string_one)
    sorted_string_two = sorted(stripped_string_two)

    if sorted_string_one != sorted_string_two:
        print("The two words, " + stripped_string_one + " and " + stripped_string_two
              + ", are not anagrams of each other.")
        return False
    else:
        print("The two words, " + stripped_string_one + " and " + stripped_string_two
              + ", are anagrams of each other.")
        return True


is_anagram(word_one, word_two)