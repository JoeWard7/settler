"""Main program Joseph Ward."""

import setup as set
import function as fun

run = True
while run:
    print("")
    print("Welcome!")
    print("")
    print("red = 1 | blue = 2 | orange = 3 | white = 4")
    player = int(input("Player: "))
    print("")
    print("What do you want to do?")
    print("1) Player Stats")
    print("2) Player Odds")
    print("3) Player Recource Odds")
    print("4) Add settle")
    print("5) Roll")
    print("6) Remove Cards")
    print("7) Game Odds")
    print("8) End")
    option = int(input("Option: "))
    if option == 1:
        if player == 1:
            print(set.red_settle)
            fun.player_statcalc(set.red_settle)
            print(set.red_hand)
            print(set.red_VP)
        elif player == 2:
            print(set.blue_settle)
            fun.player_statcalc(set.blue_settle)
            print(set.blue_hand)
            print(set.blue_VP)
        elif player == 3:
            print(set.orange_settle)
            fun.player_statcalc(set.orange_settle)
            print(set.orange_hand)
            print(set.orange_VP)
        elif player == 4:
            print(set.white_settle)
            fun.player_statcalc(set.white_settle)
            print(set.white_hand)
            print(set.white_VP)
        else:
            break
    elif option == 2:
        if player == 1:
            print(fun.player_odds(set.red_settle))
        elif player == 2:
            print(fun.player_odds(set.blue_settle))
        elif player == 3:
            print(fun.player_odds(set.orange_settle))
        elif player == 4:
            print(fun.player_odds(set.white_settle))
        else:
            break
    elif option == 3:
        if player == 1:
            print("Wood: " + fun.player_resOdds(set.red_settle, 1))
            print("Wool: " + fun.player_resOdds(set.red_settle, 2))
            print("Wheat: " + fun.player_resOdds(set.red_settle, 3))
            print("Wheat: " + fun.player_resOdds(set.red_settle, 4))
            print("Wheat: " + fun.player_resOdds(set.red_settle, 5))
        elif player == 2:
            print("Wood: " + fun.player_resOdds(set.blue_settle, 1))
            print("Wool: " + fun.player_resOdds(set.blue_settle, 2))
            print("Wheat: " + fun.player_resOdds(set.blue_settle, 3))
            print("Wheat: " + fun.player_resOdds(set.blue_settle, 4))
            print("Wheat: " + fun.player_resOdds(set.blue_settle, 5))
        elif player == 3:
            print("Wood: " + fun.player_resOdds(set.orange_settle, 1))
            print("Wool: " + fun.player_resOdds(set.orange_settle, 2))
            print("Wheat: " + fun.player_resOdds(set.orange_settle, 3))
            print("Wheat: " + fun.player_resOdds(set.orange_settle, 4))
            print("Wheat: " + fun.player_resOdds(set.orange_settle, 5))
        elif player == 4:
            print("Wood: " + fun.player_resOdds(set.white_settle, 1))
            print("Wool: " + fun.player_resOdds(set.white_settle, 2))
            print("Wheat: " + fun.player_resOdds(set.white_settle, 3))
            print("Wheat: " + fun.player_resOdds(set.white_settle, 4))
            print("Wheat: " + fun.player_resOdds(set.white_settle, 5))
        else:
            break
    elif option == 4:
        letters = [x for x in input("Letters: ").split()]
        if player == 1:
            print(set.red_settle)
            fun.add_settle(set.red_settle, letters)
            print(set.red_settle)
        elif player == 2:
            print(set.blue_settle)
            fun.add_settle(set.blue_settle, letters)
            print(set.blue_settle)
        elif player == 3:
            print(set.orange_settle)
            fun.add_settle(set.orange_settle, letters)
            print(set.orange_settle)
        elif player == 4:
            print(set.white_settle)
            fun.add_settle(set.white_settle, letters)
            print(set.white_settle)
        else:
            break
    elif option == 5:
        print("Roll: ")
        roll = int(input())
        fun.dice_roll(roll)
    elif option == 6:
        cards = [int(x) for x in input("Cards: ").split()]
        if player == 1:
            print(set.red_hand)
            fun.card_remove(set.red_hand, cards)
            print(set.red_hand)
        elif player == 2:
            print(set.blue_hand)
            fun.card_remove(set.blue_hand, cards)
            print(set.blue_hand)
        elif player == 3:
            print(set.orange_hand)
            fun.card_remove(set.orange_hand, cards)
            print(set.orange_hand)
        elif player == 4:
            print(set.white_hand)
            fun.card_remove(set.white_hand, cards)
            print(set.white_hand)
        else:
            break
    elif option == 7:
        print("Wood: " + fun.game_odds(1))
        print("Wool: " + fun.game_odds(2))
        print("Wheat: " + fun.game_odds(3))
        print("Wheat: " + fun.game_odds(4))
        print("Wheat: " + fun.game_odds(5))
    elif option == 8:
        run = False
    else:
        break
