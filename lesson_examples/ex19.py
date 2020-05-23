# defines the function cheese_and_crackers with two input variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# takes the function and gives it two arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# adds value to above function by defining variables with integers
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# takes values from above variables and puts into function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# does math and adds to each function bit
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# combines variable with math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# my function
def anthony(height, weight, pull_count):
    print("I'm Anthony.")
    print(f"I'm {height} tall and weigh {weight}.")
    print(f"But I can do {pull_count} pull-ups.")


tall = "six feet, two inches"
pounds = 198
pullz = 8
anthony(tall, pounds, pullz)

anthony(tall * 2, pounds + 5, pullz + 5)

anthony(5, 1, pullz)

anthony(10 + 20, pounds - 3, pounds - pullz)
