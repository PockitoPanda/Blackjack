from art import logo
import random, os

print(logo)

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    if 11 in hand and sum(hand) > 21:
        for card in hand:
            if card == 11:
                position = hand.index(card) 
                hand[position] = 1
                break
    return sum(hand)


def compare_score(user_score, comp_score):
    if user_score > 21:
        return ("You went over. You lose :'(")
    elif user_score > comp_score and user_score <= 21:
        return ("You WIN!~")
    elif comp_score > 21 and user_score <= 21:
        return ("Opponent went over. You win!")
    elif user_score == comp_score and user_score <= 21:
        return ("Draw")
    elif user_score < comp_score:
        return ("You lose.")


def blackjack():
    user_hand = []
    comp_hand = []
    # STARTING HANDS
    for _ in range(2):
        user_hand.append(deal())
        comp_hand.append(deal())
    user_score = calculate_score(user_hand)
    comp_score = calculate_score(comp_hand)

    still_in = True
    while still_in:
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {comp_hand[0]}")
        choose_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        os.system('cls')
        if choose_deal == "y":
            user_hand.append(deal())
            user_score = calculate_score(user_hand)
            if user_score > 21:
                still_in = False
        elif choose_deal == "n":
            still_in = False
    
    while comp_score <= 17:
        comp_hand.append(deal())
        comp_score = calculate_score(comp_hand)

    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {comp_hand}, final score: {comp_score}")

    print(compare_score(user_score, comp_score))

    play_again = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if play_again == 'y':
        os.system('cls')
        blackjack()

blackjack()




