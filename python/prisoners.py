# 100 prisoners numbered 1-100
# 100 boxes with a piece of paper with its number
# shuffle pieces of paper amongs the boxes
# prisoners enter and have 50 tries to find their number
# this is a strategy that gives a 31% chance of success

import random

SIMULATIONS = 10000
PRISONERS = 100
TRIES = 50

successes = 0
for _ in range(SIMULATIONS):
    boxes = random.sample(range(PRISONERS), PRISONERS)
    for prisoner in range(PRISONERS):
        box = boxes[prisoner]
        checked = set()
        while box != prisoner:
            checked.add(box)
            box = boxes[box]
        if len(checked) > TRIES:
            break
    else:
        successes += 1

print(f"Success rate: {successes/SIMULATIONS:.2%}")