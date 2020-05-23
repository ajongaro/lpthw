name = 'Anthony J. Ongaro'
age = 34 #not a lie
height = 74 #inches
weight = 195 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
uk_height = height * 2.54 #centimeters
uk_weight = weight / 2.2 #kilograms

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"If you're from the UK, he would be {uk_height} centimeters, and {uk_weight} kilograms!")
