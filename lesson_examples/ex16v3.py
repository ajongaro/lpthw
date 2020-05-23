print("""
from sys import argv
script = argv
print("Let's open that text, shall we?")
print("Hit return, or exit.")
input(">> ")
print("What's the name of the file again?\n >> ")
text = input()
fart = open(text)
print(f"Dope, here's your file: {text}")
print(fart.read())
""")


from sys import argv
script, filename = argv
input(f"Oh, so you want to see {filename}?\n>> ")
text = open(filename)
print(text.read())
