from collections import defaultdict

from aoc import input_as_lines, parse_positive_ints_str

inp = input_as_lines("day7.txt")

class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    def __init__(self, rank_str):
        self.rank_str = rank_str
        if rank_str == "A":
            rank_str = 14
        if rank_str == "K":
            rank_str = 13
        if rank_str == "Q":
            rank_str = 12
        if rank_str == "J":
            rank_str = 11
        if rank_str == "T":
            rank_str = 10
        self.rank = int(rank_str)

    def __str__(self):
        return self.rank_str 

    def __eq__(self, other):
        return (self.rank == other.rank)

    def __ne__(self, other):
        return (self.rank != other.rank)

    def __lt__(self, other):
        return (self.rank < other.rank)

    def __le__(self, other):
        return (self.rank <= other.rank)

    def __gt__(self, other):
        return (self.rank > other.rank)

    def __ge__(self, other):
        return (self.rank >= other.rank)

def is_five(card_count):
    return 5 in card_count.values()

def is_four(card_count):
    return 4 in card_count.values() and 1 in card_count.values()

def is_full(card_count):
    return 3 in card_count.values() and 2 in card_count.values()

def is_three(card_count):
    return 3 in card_count.values()

def is_2pair(card_count):
    return list(card_count.values()).count(2) == 2

def is_pair(card_count):
    return 2 in card_count.values()

def find_type(cards):
    card_count = defaultdict(int)
    for c in cards:
        card_count[c.rank] += 1
    if is_five(card_count):
        return "FIVE"
    if is_four(card_count):
        return "FOUR"
    if is_full(card_count):
        return "FULL"
    if is_three(card_count):
        return "THREE"
    if is_2pair(card_count):
        return "2PAIR"
    if is_pair(card_count):
        return "PAIR"
    return "HIGH"

TYPES = ("HIGH", "PAIR", "2PAIR", "THREE", "FULL", "FOUR", "FIVE")

class Hand(object):
    def __init__(self, cards, bid):
        self.cards = cards
        self.type = find_type(self.cards)
        self.type_rank = TYPES.index(self.type)
        self.bid = bid
    
    def __str__(self):
        cards_str = [str(c) for c in self.cards]
        return "".join(cards_str) + " " + self.type + " " + str(self.type_rank)
    
    def __lt__(self, other):
        if (self.type_rank < other.type_rank):
            return True
        if (self.type_rank == other.type_rank):
            for index, c in enumerate(self.cards):
                other_c = other.cards[index]
                if c == other_c:
                    continue
                return c < other_c
            
    def __gt__(self, other):
        if (self.type_rank > other.type_rank):
            return True
        if (self.type_rank == other.type_rank):
            for index, c in enumerate(self.cards):
                other_c = other.cards[index]
                if c == other_c:
                    continue
                return c > other_c
            
    def __eq__(self,other):
        if (self.type_rank != other.type_rank):
            return False
        for index, c in enumerate(self.cards):
            other_c = other.cards[index]
            if c != other_c:
                return False
        return True

hands = []
for line in inp:
    cards, bid = line.split(" ")
    h = Hand([Card(x) for x in cards], int(bid))
    hands.append(h)

ss = sorted(hands)
rank = 1
sum = 0
for s in ss:
    sum += rank * s.bid
    rank+=1

print(sum)