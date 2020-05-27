# dice game using Functions

import random

def win (bety, banky):
    print(f"You won that one.")
    winnings = int(bety) * 2
    new_bal = winnings + banky
    print(f"You win ${winnings} and have ${new_bal} total, now.")
    return new_bal


def lose (bety, banky, count):
    print(f"Looks like I did it in {count - 1} tries.")
    new_bal = banky - bety
    print(f"You lost ${bety} and have ${new_bal} left.")
    return new_bal


def roll (rolls, bet_money, stash):
    d1 = 1
    d2 = 2
    while rolls < 5 and d1 != d2:
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        rolls += 1
        print(f"I rolled {d1} & {d2}")
    if d1 != d2 and rolls >= 5:
        new_bal = win(bet_money, stash)
        return new_bal
    else:
        new_bal = lose(bet_money, stash, rolls)
        return new_bal


play_again = input("Let's play a game. You down? [y/n]: ")
if play_again == 'y':
    bankroll = int(input("How much money do you even have? $"))
    while play_again == 'y':
        your_bet = int(input(f"Okay. You have ${bankroll} in your stash. What's your bet? $"))
        print(f"Cool, you have {your_bet} at risk and {bankroll - your_bet} left over.")
        print("If I roll a pair in 10 shots, I win. If I don't, you win.")
        bankroll = roll(1, your_bet, bankroll)
        if bankroll <= 0:
            print("You're done, bruh.")
            break
        else:
            play_again = input("Okay, play again? [y/n]: ")

print("Oh? Bye.")
