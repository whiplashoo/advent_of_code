inp = "172851-675869"

low = int(inp.split("-")[0])
high = int(inp.split("-")[1])


count = 0
for num in range(low, high):
    digits = [int(x) for x in str(num)]
    is_valid = True
    has_same = False
    for a, b in zip(digits, digits[1:]):
        if a == b and digits.count(a) == 2:
            has_same = True
        if a > b:
            is_valid = False
            break
    if is_valid and has_same:
        count += 1

print(count)
