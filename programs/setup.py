"""Setup and Storage."""

if __name__ == "__main__":
    print("Hey, you called me directly. Nice.")
else:
    print("Hmm, you imported me. My name, therefore, is " + __name__)

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

player_name = {
    "Red": "Jack", "Blue": "Joe", "Orange": "John", "White": "James"
}

print("Please enter players:")
for name in player_name:
    print(name + ": ", end="")
    x = input()
    if x == "q":
        break
    else:
        player_name[name] = x

# player red set
red_settle = ["A", "B", "C", "D", "E", "O"]
print("Please enter red players letters:")
red_settle = [x for x in input("Starting Letters: ").split()]
red_hand = [1, 2, 3, 4, 5]

# player blue set
blue_settle = ["F", "G", "H", "I", "J", "O"]
print("Please enter blue players letters:")
blue_settle = [x for x in input("Starting Letters: ").split()]
blue_hand = [1, 2, 3, 4, 5]

# player orange set
orange_settle = ["A", "B", "C", "D", "E", "O"]
print("Please enter orange players letters:")
orange_settle = [x for x in input("Starting Letters: ").split()]
orange_hand = [1, 2, 3, 4, 5]

# player white set
white_settle = ["A", "B", "C", "D", "E", "O"]
print("Please enter white players letters:")
white_settle = [x for x in input("Starting Letters: ").split()]
white_hand = [1, 2, 3, 4, 5]
