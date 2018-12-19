"""Probability's by Joseph Ward."""

# game setup
resource_position = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 1, "G": 2, "H": 3, "I": 4,
    "J": 5, "K": 1, "L": 2, "M": 3, "N": 4, "O": 1, "P": 1, "Q": 2, "R": 3
}

print("Please enter recource for each chip:")
for letter in resource_position:
    print(letter + ": ", end="")
    x = input()
    if x == "q":
        break
    else:
        resource_position[letter] = int(x)
print(resource_position)

letter_num = {
    "A": 5, "B": 2, "C": 6, "D": 3, "E": 8, "F": 10, "G": 9, "H": 12, "I": 11,
    "J": 4, "K": 8, "L": 10, "M": 9, "N": 4, "O": 5, "P": 6, "Q": 3, "R": 11,
    "robber": 7
}

letter_probs = {
    "A": 4 / 36, "B": 1 / 36, "C": 5 / 36, "D": 2 / 36, "E": 5 / 36,
    "F": 3 / 36, "G": 4 / 36, "H": 1 / 36, "I": 2 / 36, "J": 3 / 36,
    "K": 5 / 36, "L": 3 / 36, "M": 4 / 36, "N": 3 / 36, "O": 4 / 36,
    "P": 5 / 36, "Q": 2 / 36, "R": 2 / 36, "robber": 6 / 36
}

resource_index = {
    1: "wood", 2: "wool", 3: "wheat", 4: "brick", 5: "ore"
}

player_color = {
    "Red": 1, "Blue": 2, "Orange": 3, "White": 4
}

print("Please enter players:")
for color in player_color:
    print(color + ": ", end="")
    x = input()
    if x == "q":
        break
    else:
        player_color[color] = x

# player one set
red_settle = ["A", "B", "C", "D", "E", "O"]
print("Please enter red players letters:")
red_settle = [x for x in input("Starting Letters: ").split()]
red_hand = [1, 2, 3, 4, 5]

# player two set
blue_settle = ["F", "G", "H", "I", "J", "O"]
print("Please enter blue players letters:")
blue_settle = [x for x in input("Starting Letters: ").split()]
blue_hand = [1, 2, 3, 4, 5]

# player three set
orange_settle = ["A", "B", "C", "D", "E", "O"]
print("Please enter orange players letters:")
orange_settle = [x for x in input("Starting Letters: ").split()]
orange_hand = [1, 2, 3, 4, 5]

# player four set
white_settle = ["A", "B", "C", "D", "E", "O"]
print("Please enter white players letters:")
white_settle = [x for x in input("Starting Letters: ").split()]
white_hand = [1, 2, 3, 4, 5]


def player_statcalc(player):
    """Print this."""
    player_prop = []
    player_res = []
    player_num = []
    for letter in player:
        prob = letter_probs[letter]
        resIndex = resource_position[letter]
        res = resource_index[resIndex]
        num = letter_num[letter]
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
        if resource_position[letter] == resNum:
            resource_list.append(letter)
    return player_odds(resource_list)


def add_settle(player, settles):
    """Print me."""
    print(settles)
    for letter in settles:
        player.append(letter)


print(player_resOdds(red_settle, 1))
print(player_odds(red_settle))

player_statcalc(red_settle)
print(red_settle)
add_settle(red_settle, ["Q", "F"])
player_statcalc(red_settle)
print(red_settle)

print(player_resOdds(blue_settle, 1))
print(player_odds(blue_settle))

player_statcalc(blue_settle)
print(blue_settle)
add_settle(blue_settle, ("B"))
player_statcalc(blue_settle)
print(blue_settle)
