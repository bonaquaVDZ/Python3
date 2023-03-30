""""Find Xth number in a list which is sorted in ascending order."""

def get_x(x, nums):
    """"Find Xth Number in ascending order."""
    if x > len(nums) or x == 0:
        return 0
    else:
        nums = sorted(nums)
        return nums[x-1]

print(get_x(3, [-3, 100, 2, 10, 31]))
