from typing import List

def moveZeroes(nums: List[int]) -> None:
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)