from aoc import input_as_lines

inp = input_as_lines("day4.txt")

numbers = [int(x) for x in inp[0].split(',')]

bingo_cards = []
bingo_checks = []

temp_card = []
for line in inp[2:]:
    if line is not "":
        temp_card.append([int(x) for x in line.split()])
    else:
        bingo_cards.append(temp_card)
        bingo_checks.append([[0 for col in range(5)] for row in range(5)])
        temp_card = []

bingo_cards.append(temp_card)
bingo_checks.append([[False for col in range(5)] for row in range(5)])
cards_that_won = [False for x in bingo_cards]

# PART 1


def check_column(m, column):
    for row in range(len(m)):
        if not m[row][column]:
            return False
    return True


def unmarked_sum(card_index):
    s = 0
    for row in range(5):
        for col in range(5):
            if not bingo_checks[card_index][row][col]:
                s += bingo_cards[card_index][row][col]
    return s


def check_card(card_index, row, col):
    # check horizontally
    if all(bingo_checks[card_index][row]):
        return unmarked_sum(card_index)
    # check vartically
    if check_column(bingo_checks[card_index], col):
        return unmarked_sum(card_index)
    return False


def run_draw():
    for draw in numbers:
        for card_index in range(len(bingo_cards)):
            for row in range(5):
                for col in range(5):
                    if bingo_cards[card_index][row][col] == draw:
                        bingo_checks[card_index][row][col] = True
                        check_result = check_card(card_index, row, col)
                        if check_result is not False:
                            print("Bingo!")
                            print(check_result*draw)
                            # PART 2
                            cards_that_won[card_index] = True
                            if all(cards_that_won):
                                print("ALL WON!")
                                return(unmarked_sum(card_index)*draw)
                            # return(check_result*draw)


# run_draw()
print(run_draw())
