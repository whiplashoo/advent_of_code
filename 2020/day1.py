def findpair(nums, pairsum):
	left = 0
	right = len(nums) - 1
	nums = sorted(nums)
	print(nums)
	while left<right:
		sum = nums[left] + nums[right]
		if sum == pairsum:
			return nums[left] * nums[right]
		elif sum > pairsum:
			right -= 1
		else:
			left += 1

def findthree(nums, target):
	nums = sorted(nums)
	print(nums)
	for i in range(len(nums)-1):
		left = i + 1
		right = len(nums) - 1
		while left < right:
			sum = nums[left] + nums[right] + nums[i]
			if sum == target:
				return nums[left] * nums[right] * nums[i]
			elif sum > target:
				right -= 1
			else:
				left += 1

nums = []

with open("day1.txt") as f:
	for line in f:
		nums.append(int(line))	
	#print(findpair(nums, 2020))
	print(findthree(nums, 2020))

	
