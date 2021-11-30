def check_valid(num, prev25):
    left = 0
    right = len(prev25) - 1
    prev25 = sorted(prev25)
    while left < right:
        sum = prev25[left] + prev25[right]
        if sum == num:
            return True
        elif sum > num:
            right -= 1
        else:
            left += 1
    return False


def part_one(nums):
    for i, num in enumerate(nums):
        if i >= 25:
            prev25 = nums[i - 25:i]
            if not check_valid(num, prev25):
                return num


def part_two(nums):
    target = part_one(nums)
    for i in range(len(nums)):
        temp_list = []
        sum = 0
        for j in nums[i:]:
            sum += j
            temp_list.append(j)
            if sum == target:
                print(temp_list)
                return min(temp_list) + max(temp_list)
            if sum > target:
                break


with open("day9.txt") as f:
    nums = []
    for line in f:
        nums.append(int(line.strip()))
    print(part_one(nums))
    print(part_two(nums))
