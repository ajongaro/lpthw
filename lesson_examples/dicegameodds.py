# Roll a dice 10 times and see if a pair is rolled
# Repeat that 1000 times and count number of pairs hit within 10 rolls out of 1000 'games'
# Adjust number of rolls to improve or reduce odds of winning to > 48% and < 52%
# Stop operation when success % is in that range and return the # of rolls needed for this game.

import random

def roll (rolls, arolls):
    d1 = 1
    d2 = 2
    while rolls < arolls and d1 != d2:
        d1 = random.randint(1, 20)
        d2 = random.randint(1, 20)
        rolls += 1
        print(f"[{rolls}] I rolled {d1} & {d2}")
    if d1 != d2 and rolls <= arolls:
        win = True
        return win
    else:  # This will not add to win count
        win = False
        return win


play_count = 0
game_result = 0
num_of_wins = 0
adjusted_rolls = 10
simulations = 0


while not 4800 <= num_of_wins < 5200:
    while play_count < 10000:
        game_result = roll(0, adjusted_rolls)
        print(f"Win? {game_result}.")
        if game_result == True:
            num_of_wins += 1
            play_count += 1
            print(f"Wins are {num_of_wins}, count is {play_count}.")
        else:
            play_count += 1
            print(f"Wins are {num_of_wins}, count is {play_count}.")
#    else:
    if num_of_wins < 4800:
        adjusted_rolls -= 1
        play_count = 0
        num_of_wins = 0
        simulations += 1
    elif num_of_wins > 5200:
        adjusted_rolls += 1
        play_count = 0
        num_of_wins = 0
        simulations += 1
    else:
        play_count = 0
        simulations +=1

print(f"I've calculated {adjusted_rolls} as the perfect number for {num_of_wins} wins out of 10000 games.")
print(f"It only took me {simulations} simulations.")
