"""Probability's by Joseph Ward."""

# "A": 5, "B": 2, "C": 6, D": 3, "E": 8, "F": 10, "G": 9, "H": 12, "I": 11,
# "J": 4, "K": 8, "L": 10, "M": 9, "N": 4, "O": 5, "P": 6, "Q": 3, "R": 11

# playerone = blue
# playertwo = red
# playerthree = orange
# playerfour = white

letter_probs = {
    "A": 4 / 36, "B": 1 / 36, "C": 5 / 36, "D": 2 / 36, "E": 5 / 36,
    "F": 3 / 36, "G": 4 / 36, "H": 1 / 36, "I": 2 / 36, "J": 3 / 36,
    "K": 5 / 36, "L": 3 / 36, "M": 4 / 36, "N": 3 / 36, "O": 4 / 36,
    "P": 5 / 36, "Q": 2 / 36, "R": 2 / 36
}

letter_resource = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 1,
    "G": 2,
    "H": 3,
    "I": 4,
    "J": 5,
    "K": 1,
    "L": 2,
    "M": 3,
    "N": 4,
    "O": 5,
    "P": 1,
    "Q": 2,
    "R": 3
}

resource_num = {
    1: "wood",
    2: "wool",
    3: "wheat",
    4: "brick",
    5: "ore"
}

playerone_settle = ["A", "B", "C", "D", "E", "F", "G"]
playerone_prop = []
playerone_res = []

for letter in playerone_settle:
    prob = letter_probs[letter]
    resNum = letter_resource[letter]
    res = resource_num[resNum]
    playerone_prop.append(prob)
    playerone_res.append(res)

totalProb = 0.0
for  in playerone_prop:
    totalProb += playerone_prop[prob]
    print(totalProb)

print(playerone_prop)
print(playerone_res)
