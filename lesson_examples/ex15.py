# imports argv module from sys(tem?)
from sys import argv
# names script, filename as argv
# script, filename = argv
script = argv

txt = input(f"What's that filename?\n>> ")
file = open(txt)
print(f"Cool, here's your file {txt}.")
print(file.read())
