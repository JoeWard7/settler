"""Main program Joseph Ward."""

import setup as set
import function as fun
print(__name__)
if __name__ == "__main__":
    print("Hey, you called me directly. Nice.")
else:
    print("Hmm, you imported me. My name, therefore, is " + __name__)

print(fun.player_resOdds(set.red_settle, 1))
print(fun.player_odds(set.red_settle))

fun.player_statcalc(set.red_settle)
print(set.red_settle)
fun.add_settle(set.red_settle, ["Q", "F"])
fun.player_statcalc(set.red_settle)
print(set.red_settle)

print(fun.player_resOdds(set.blue_settle, 1))
print(fun.player_odds(set.blue_settle))

fun.player_statcalc(set.blue_settle)
print(set.blue_settle)
fun.add_settle(set.blue_settle, ("B"))
fun.player_statcalc(set.blue_settle)
print(set.blue_settle)
