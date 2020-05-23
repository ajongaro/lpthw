# defines types_of_people variable, set to 10
types_of_people = 10
# defines x variable as a string of text that also displays types of people variable
x = f"There are {types_of_people} types of people."
# creates a variable that just repeats the title, but as a defined variable/vs printed txt string
binary = "binary"
# creates a variable that abreviates itself
do_not = "don't"
# new variable, simple print with variables in a f-string
y = f"Those who know {binary} and those who {do_not}."
# displaying the above x/y variables in sequence
print(x)
print(y)
# printing the f-string repeating the above varibles by including in f-string
print(f"I said: {x}")
print(f"I also said: {y}")
# defining hilarious variable as False
hilarious = True
# setting joke_evaluation variable, but I don't get why there's squiggles here.
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
