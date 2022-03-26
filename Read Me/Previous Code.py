import random
import sys

Shape = ["♣", "♦", "♥", "♠"]
rank = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
card_deck = []
omi_deck = []

first_shuffle_player = []
first_shuffle_bot = []
second_shuffle_player = []
second_shuffle_bot = []

player_hand = []
bot_hand = []

user_playing = []
bot_playing = []

all_trump = []

empty_space = " "
numbers = [1, 2, 3, 4]
trump_suit = ""

my_dict = {}

Trick = 1

player_score = 0
bot_score = 0

trick_winner = "bot"
win = "bot"


# intro of the game
def start_game():
    print("Welcome to OMI")
    print("You can play until you get bored :) (infinite rounds")
    print ("Every round has 8 tricks")
    print ("2 points will be given to the winner in each trick")
    print ("If you win all the tricks, you will be marked as the 'lEGEND' ")
    print("Here you wil see different kind of cards(shape+number) and each cards has it's own value")
    print("A=14,K=13,Q=12,J=11,10=10,9=9,8=8,7=7")
    print("Shapes = ♣, ♦, ♥, ♠ (shape has no value until you select it as the 'TRUMP')")


    print ("Good luck")

    print("You are responsible to choose the trump suit""\n")


# creating a MAIN desk with 52 cards
def creating_deck():
    for i in rank:
        for j in Shape:
            card_deck.append(str(i) + (j))


# getting only 32 cards from the main desk for OMI
def omi_cards():
    for i in rank[0:8]:
        for j in Shape:
            omi_deck.append(str(i) + (j))


# first shuffle for human
def first_shuffling_p():
    i = 0
    while i != 4:
        rand = random.choice(duplicate_omi)
        if (rand not in first_shuffle_player and rand not in second_shuffle_player and
                rand not in first_shuffle_bot and rand not in second_shuffle_bot):
            first_shuffle_player.append(rand)
            i = i + 1
    print("Your hand is :", first_shuffle_player)


# second shuffle for human
def second_shuffling_p():
    i = 0
    while i != 4:
        rand = random.choice(duplicate_omi)
        if (rand not in first_shuffle_player and rand not in second_shuffle_player and
                rand not in first_shuffle_bot and rand not in second_shuffle_bot):
            second_shuffle_player.append(rand)
            i = i + 1


# first shuffle for bot
def first_shuffling_b():
    i = 0
    while i != 4:
        rand = random.choice(duplicate_omi)
        if (rand not in first_shuffle_player and rand not in second_shuffle_player and
                rand not in first_shuffle_bot and rand not in second_shuffle_bot):
            first_shuffle_bot.append(rand)
            i = i + 1


# second shuffle for bot
def second_shuffling_b():
    i = 0
    while i != 4:
        rand = random.choice(duplicate_omi)
        if (rand not in first_shuffle_player and rand not in second_shuffle_player and
                rand not in first_shuffle_bot and rand not in second_shuffle_bot):
            second_shuffle_bot.append(rand)
            i = i + 1


# trump choosing, for player.
def selecting_trump():
    global trump
    print()
    print("NOTE : TYPE 1 for '♣' , 2 for '♦', 3 for '♥', 4 for '♠'""\n")
    trump = input("Please enter the trump : ")


# user entering a card from his hand
def user_call():
    global u_call
    u_call = input("Your call : ")


def bot_call():
    global b_call
    b_call = random.choice(bot_hand)
    return b_call

def bot_call_2():
    global b_call_2
    global winner_new
    b_call_2 = random.choice(bot_hand)



def all_trump_cards ():
    for i in player_hand:
        if any(trump_suit in s for s in i):
            all_trump.append(i)

def card_validity ():
    while u_call not in player_hand:
        print("It's not in player hand, Enter a valid card")
        user_call()
    else:
        shape_check_123()

def shape_check_123():
    global winner
    if len(b_call) == 2:
        if any (b_call[1] in s for s in player_hand):
            if b_call[1] not in u_call:
                while b_call[1] not in u_call:
                    print("Check your card's shape")
                    user_call()
            else:
                dict_bot()
                dict_player()
                max_key = max(my_dict, key=my_dict.get)
                if max_key in u_call:
                    winner = "player"
                    print("Player wins + 2")

                elif max_key in b_call:
                    winner = "bot"
                    print ("Robot wins + 2")

        else:
            if u_call in all_trump:
                winner = "player"
                print("Player wins + 2")
            else:
                winner = "bot"
                print ("Robot wins + 2")
                pass

    elif len(b_call) == 3:
        if any (b_call[2] in s for s in player_hand):
            if b_call[2] not in u_call:
                while b_call[2] not in u_call:
                    print("Check your card's shape")
                    user_call()
            else:
                dict_bot()
                dict_player()
                max_key = max(my_dict, key=my_dict.get)
                if max_key in u_call:
                    winner = "player"
                    print ("Player wins + 2")

                elif max_key in b_call:
                    winner = "bot"
                    print ("Robot wins + 2")
        else:
            if u_call in all_trump:
                winner = "player"
                print ("Player wins + 2")
            else:
                winner = "bot"
                print ("Robot wins + 2")
                pass
    return winner

def card_validity_2 ():
    while u_call not in player_hand:
        print("It's not in player hand")
        user_call()
    else:
        shape_check_1234()

def shape_check_1234():
    global max_key
    bot_call()
    if len(u_call) == 2:
        if any (u_call[1] in s for s in bot_hand):
            if len(b_call) == 2:
                if b_call[1] not in u_call:
                    while b_call[1] not in u_call:
                        bot_call()
                else:
                    pass

            elif len(b_call) == 3:
                if b_call[2] not in u_call:
                    while (b_call[2]) not in (u_call):
                        bot_call()
                else:
                    pass
        else:
            pass

    elif len(u_call) == 3:
        if any (u_call[2] in s for s in bot_hand):
            if len(b_call) == 2:
                if b_call[1] not in u_call:
                    while b_call[1] not in u_call:
                        bot_call()
                else:
                    pass

            elif len(b_call) == 3:
                if b_call[2] not in u_call:
                    while b_call[2] not in u_call:
                        bot_call()
                else:
                    pass
        else:
            pass

    return b_call

def dict_player():
    if u_call[0] == "A":
        my_dict["A"] = 14
    elif u_call[0] == "K":
        my_dict["K"] = 13
    elif u_call[0] == "Q":
        my_dict["Q"] = 12
    elif u_call[0] == "J":
        my_dict["J"] = 11
    elif u_call[0] == "1":
        my_dict["1"] = 10
    elif u_call[0] == "9":
        my_dict["9"] = 9
    elif u_call[0] == "8":
        my_dict["8"] = 8
    elif u_call[0] == "7":
        my_dict["7"] = 7

def dict_bot ():
    if b_call[0] == "A":
        my_dict["A"] = 14
    elif b_call[0] == "K":
        my_dict["K"] = 13
    elif b_call[0] == "Q":
        my_dict["Q"] = 12
    elif b_call[0] == "J":
        my_dict["J"] = 11
    elif b_call[0] == "1":
        my_dict["1"] = 10
    elif b_call[0] == "9":
        my_dict["9"] = 9
    elif b_call[0] == "8":
        my_dict["8"] = 8
    elif b_call[0] == "7":
        my_dict["7"] = 7

def replay():
    global r_play
    r_play = input("You wanna play ? (yes/no) : ")

replay()
if r_play == "n" or r_play == "N":
        print ("END OF THE GAME")
        sys.exit()   #<----exiting the game

while r_play == "y" or r_play == "Y":
    start_game()
    creating_deck()
    duplicate_deck = tuple(card_deck)
    omi_cards()
    duplicate_omi = tuple(omi_deck)

    first_shuffling_p()
    second_shuffling_p()
    first_shuffling_b()
    second_shuffling_b()

    player_hand = first_shuffle_player + second_shuffle_player
    bot_hand = first_shuffle_bot + second_shuffle_bot

    selecting_trump()

    while trump not in str(numbers):
        print(empty_space * 10, "WRONG ENTRY, TRY AGAIN..")
        selecting_trump()
    else:

        print()
        print("Let's play")
        print()

        while Trick <= 8:

            if trump == "1":
                trump_suit = "♣"
            elif trump == "2":
                trump_suit = "♦"
            elif trump == "3":
                trump_suit = "♥"
            elif trump == "4":
                trump_suit = "♠"

            if any(trump_suit in s for s in first_shuffle_player):

                print("Trick ", Trick)
                print("Trump suit : ", trump_suit)
                print("Your hand : ", player_hand)
                all_trump_cards()

                if trick_winner == "player":
                    user_call()
                    card_validity_2()

                    shape_check_1234()
                    print("Robot says : ", b_call)

                    dict_player()
                    dict_bot()
                    max_key = max(my_dict, key=my_dict.get)

                    if u_call in all_trump and trump_suit in b_call:
                        if max_key in u_call:
                            print("Player wins + 2")
                            winner = "player"
                        else:
                            print("Robot wins + 2")
                            winner = "bot"
                    elif u_call in all_trump and trump_suit not in b_call:
                        print("Player wins + 2")
                        winner = "player"
                    else:
                        if max_key in u_call:
                            print("Player wins + 2")
                            winner = "player"
                        else:
                            print("Robot wins + 2")
                            winner = "bot"

                    player_hand.remove(u_call)
                    bot_hand.remove(b_call)
                    all_trump.clear()
                    my_dict.clear()

                    trick_winner = winner

                    if trick_winner == "player":
                        player_score = player_score + 2
                    elif trick_winner == "bot":
                        bot_score = bot_score + 2

                    print()
                    Trick = Trick + 1


                elif trick_winner == "bot":
                    print("Robot says : ", bot_call())

                    # Testing whether the shape is in or not
                    if len(b_call) == 2:
                        if any(b_call[1] in s for s in player_hand):
                            print("That shape is in your hand")
                        else:
                            print("That shape is not in your hand. So you can use any card")
                    elif len(b_call) == 3:
                        if any(b_call[2] in s for s in player_hand):
                            print("That shape is in your hand")
                        else:
                            print("That shape is not in your hand. So you can use any card")

                    # Testing whether all the trumps are identifiable and then appending them to a list.
                    # ----------------------------------------------

                    user_call()
                    card_validity()

                    # ----------------------------------

                    player_hand.remove(u_call)
                    bot_hand.remove(b_call)
                    all_trump.clear()
                    my_dict.clear()

                    trick_winner = winner

                    if trick_winner == "player":
                        player_score = player_score + 2
                    elif trick_winner == "bot":
                        bot_score = bot_score + 2

                    print()
                    Trick = Trick + 1
            else:
                print()
                print(empty_space * 10, "ATTENTION")
                print("That shape is not in your hand for now")
                print("Please select another shape""\n")
                selecting_trump()
                print("Let's Play")
                print()
        else:
            print("Player score is : ", player_score)
            print("Bot_score is : ", bot_score)
            if player_score > bot_score:
                print("Player wins the round")
            elif player_score < bot_score:
                print("Robot wins the round")
            print("Game finished")
            Trick = 0
            card_deck.clear()
            omi_deck.clear()
            first_shuffle_player.clear()
            second_shuffle_player.clear()
            first_shuffle_bot.clear()
            second_shuffle_bot.clear()
            player_hand.clear()
            bot_hand.clear()
            player_score = 0
            winner = "bot"


            replay()