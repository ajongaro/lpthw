from sys import argv
# improts the argv module
script, filename = argv
# tells terminal how to launch w/ app name and a file filename
print(f"We're going to erase {filename}.")
# simple print, saying we're going to erase the given file filename
print("If you don't want that, hit CTRL-C (^C)")
# basic print w/ instructions
print("If you do want that, hit RETURN")
# basic print w/ input instructions

input("?")
# prompts for input with a ?

print("Opening the file...")
target = open(filename, 'w')
# defines target ... not sure what else
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
