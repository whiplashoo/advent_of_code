from aoc import parse_ints_str

with open("day6.txt") as f:
    inp = parse_ints_str(f.read().rstrip("\n"))

# PART 1 &
# PART 2
fishes = [inp.count(i) for i in range(9)]
for i in range(256):
    next_fish = fishes.pop(0)
    fishes[6] += next_fish
    fishes.append(next_fish)
print(sum(fishes))
