"""Calculations and Fucntions."""

import setup as set

if __name__ == "__main__":
    print("Hey, you called me directly. Nice.")
else:
    print("Hmm, you imported me. My name, therefore, is " + __name__)


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
    return player_odds(resource_list)


def add_settle(player, settles):
    """Print me."""
    print(settles)
    for letter in settles:
        player.append(letter)
