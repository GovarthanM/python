from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    return [nums[i // 2 + (i % 2) * n] for i in range(2 * n)]

print(shuffle([2,5,1,3,4,7], 3))
