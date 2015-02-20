__author__ = 'Omar'

# Read and write to a file
# Need two functions: one that will take text
# from the user and print it to a file.
# The other function must be able to take that
# file and print it back out to the user.

filename = "user_text.txt"


def print_to_file(text_file):
    print("Enter some text to put into the file:")
    user_input = input("---> ")
    stripped_user_input = user_input.strip()
    file = open(text_file, "w")
    file.write(stripped_user_input)
    file.close()


def read_from_file(text_file):
    file = open(text_file, "r")
    for line in file:
        print(line, end='')
    file.close()


print_to_file(filename)
read_from_file(filename)