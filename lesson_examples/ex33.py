def chill(how_many, how_much):
    i = 0
    numbers = []
    while i < how_many:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += how_much
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")
    for num in numbers:
        print(num)


times = int(input('Times > '))
leaps = int(input('Units > '))

chill(times, leaps)
