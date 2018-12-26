"""Calculations and Fucntions."""

import setup as set


def player_statcalc(player):
    """Print this."""
    player_prop = []
    player_res = []
    player_num = []
    for letter in player:
        prob = set.letter_probs[letter]
        resIndex = set.resource_position[letter]
        res = set.resource_index[resIndex]
        num = set.letter_num[letter]
        player_prop.append(prob)
        player_res.append(res)
        player_num.append(num)
    print(player_prop)
    print(player_res)
    print(player_num)


def player_odds(player):
    """Print this."""
    total = 0.0
    if "B" in player:
        total += 1
    if "D" in player or "Q" in player:
        total += 2
    if "J" in player or "N" in player:
        total += 3
    if "A" in player or "O" in player:
        total += 4
    if "C" in player or "P" in player:
        total += 5
    if "E" in player or "K" in player:
        total += 5
    if "G" in player or "M" in player:
        total += 4
    if "F" in player or "L" in player:
        total += 3
    if "I" in player or "R" in player:
        total += 2
    if "H" in player:
        total += 1
    return total / 36


def player_resOdds(player, resNum):
    """Print this."""
    resource_list = []
    for letter in player:
        if set.resource_position[letter] == resNum:
            resource_list.append(letter)
    return str(player_odds(resource_list))


def add_settle(player, settles):
    """Print me."""
    print(settles)
    for letter in settles:
        player.append(letter)


def dice_roll(roll):
    """Print me."""
    for letter in set.letter_num:
        if set.letter_num[letter] == roll:
            for ownership in set.red_settle:
                if ownership == letter:
                    set.red_hand.append(set.resource_position[letter])
            for ownership in set.blue_settle:
                if ownership == letter:
                    set.blue_hand.append(set.resource_position[letter])
            for ownership in set.orange_settle:
                if ownership == letter:
                    set.orange_hand.append(set.resource_position[letter])
            for ownership in set.white_settle:
                if ownership == letter:
                    set.white_hand.append(set.resource_position[letter])


def card_remove(player, cards):
    """Print me."""
    print(cards)
    for card in cards:
        player.remove(card)


def game_odds(resNum):
    """Print me."""
    resource_list = []
    for letter in set.resource_position:
        if set.resource_position[letter] == resNum:
            resource_list.append(letter)
    print(resource_list)
    return str(player_odds(resource_list))
