import re
import random

words = ["apple", "printer", "school", "island", "balloon", "roads", "shorts", "bottle", "voilet"]

def flip_coin(): return random.choice([True, False])
def random_word(): return random.choice(words)
def num_or_not(): return random.randint(0, 100) if flip_coin() else ""
def random_mix(): return f"{num_or_not()}{random_word()}{num_or_not()}"

with open("random_words.txt", "w") as file:
    lines = 20
    for _ in range(lines):
        file.write(f"{random_mix()} {random_mix()} {random_mix()} {random_mix()}\n")

with open("random_words.txt", "r") as file:
    print(re.findall(r"\d\d","".join(file.readlines())))
    