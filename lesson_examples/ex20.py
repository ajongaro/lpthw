# ex20 from LPTHW

# import argv module from sys
from sys import argv
# launch script with name of text file (test.txt)
script, input_file = argv
# defining function with name 'print_all' and takes argument from call as 'f'
def print_all(f):
    # prints whatever was assigned to the f variable using the read command.
    print(f.read())
# defines new function 'rewind' with another variable f assigned through a call
def rewind(f):
    # resets f to 0 bit location (begining of the 'tape')
    f.seek(0)
# defines print_a_line asking for 2 arguments, to be assigned as line_count & f respectively
def print_a_line(line_count, f):
    print(f"What's the line count?", line_count)
    # prints whatever was assigned to line_count, and current line in txt doc
    print(line_count, f.readline())
# opens the input file from original argv at top of script
current_file = open(input_file)
# simple print with new line
print("First let's print the whole file:")
# calls the print_all function, assigns current_file to f
print_all(current_file)
# simple print
print("Now let's rewind, kind of like a tape.")
# calls rewind function, assigns current_file to f
rewind(current_file)
# simple print
print("Let's print three lines:")
# assign value of 1 to current_line
current_line = 1
# calls print_a_line function while assigning current line to line_count and current_file to f
print_a_line(current_line, current_file)
# adds one to current_line count
current_line += 1
# same as above but now with 2nd line
print_a_line(current_line, current_file)
# same as above but adding one to current_line
current_line += 1
print_a_line(current_line, current_file)
