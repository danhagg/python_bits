# open() function takes one argument (name of file to open)
# as current file "File_Exceptions" is running python looks in same directory
# open function returns object stored as file_object
# keyword "with" closes file once access to it no longer needed
# (relative file path) from folder, assumes folder is in current directory
with open('text_files/pi_digits.txt') as file_object_1:
    contents = file_object_1.read(3)  # char to read
    # rstrip removes (if any) whitespace at right end of string
    print(contents.rstrip())

# (absolute file path)
# store absolute filepath in a variable and pass that to open()
absolute_file_path = '/Users/danielhaggerty/Google Drive/py/crash/text_files/pi_digits.txt'
with open(absolute_file_path) as file_object_2:
    size_to_read = 9
    contents = file_object_2.read(size_to_read)
    print(contents.rstrip())

# string tells python where to find file
# makes it easy to swap out pi_digits.txt for another file
filename = 'pi_digits.txt'
with open(filename) as file_object:
    # for loop is easier memory load
    # and does not risk opening huge file all at once
    for line in file_object:
        print(line)  # or print(line.rstrip()) to remove blanks

# or p remove blanks
filename = 'pi_digits.txt'
with open(filename) as file_object_3:
    # readlines makes a list in "lines" we can work with after "with" closes file
    lines = file_object_3.readlines()
    print(lines)
    # remove all whitespace
    pi_string = ''
    for line in lines:
        pi_string += line.strip()  # int() or float() if needed

    print(pi_string)
    print(len(pi_string))

filename = 'chapter_10/pi_million_digits.txt'
with open(filename) as file_object_4:
    # readlines makes a list in "lines" we can work with after "with" closes file
    lines = file_object_4.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

    print(pi_string[:52] + "...")
    print(len(pi_string))
birthday = "220280"
if birthday in pi_string:
    print("Your birthday is in first million digits of pi")
else:
    print("Your bday is not in there")
print(pi_string.find(birthday))
print(pi_string[332417:332423])

# writing to empty file. Python only write strings to file + str()
filename_alpha = 'programming.txt'
# 'w' = write mode/ONLY new files, will erase files with content
with open(filename_alpha, 'w') as file_object_5:
    file_object_5.write("I love programming.\n")  # write() method
    file_object_5.write("I love creating new games.\n")  # write() method

# 'a' = append
filename_alpha = 'programming.txt'
with open(filename_alpha, 'a') as file_object_5:
    file_object_5.write("I love appending shit.\n")

# 'r' = read (default if arg omitted), 'r+' = read and write

# python uses objects called exceptions (try-except) to
# manage errors that arise during a progs execution
# error = create exception obj. Handle it or prog halts + traceback
# try-except means progs run even if things go wrong

# print(5/0) yields an exception object ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print("you cant divide by zero")

# allowing users to see tracebacks exposes your vulnerabilities and filenames
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# try-except-else block
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#         second_number = input("\nSecond number: ")
#         try:
#             answer = int(first_number) / int(second_number)
#         except ZeroDivisionError:
#             print("You cant divide by zero")
#         else:
#             print(answer)

# File not found error
def count_words(filename):
    """Count words in files"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:  # when looking for 'trainspotting.txt'
        msg = "Sorry, the file " + filename + " does not exist."
        # "pass' to fail silently
        print(msg)
    else:
        # Count the approx number words in file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " contains about " +
        str(num_words) + " words")


filenames = ['chapter_10/alice.txt', 'chapter_10/trainspotting.txt',
'chapter_10/moby_dick.txt', 'chapter_10/little_women.txt']
for filename in filenames:
    count_words(filename)

# Using json
import json
numbers = [2, 3, 5, 7, 11, 13]
filename_j = 'numbers.json'
with open(filename_j, 'w') as f_obj_j:
    json.dump(numbers, f_obj_j)

filename_k = 'numbers.json'
with open(filename_k) as f_obj_k:
    numbers_k = json.load(f_obj_k)
    print("These are the numbers " + str(numbers_k))
