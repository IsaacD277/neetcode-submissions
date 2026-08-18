import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        if 0 in nums:
            result = [0 for _ in range(len(nums))]
            positions = [index for index, value in enumerate(nums) if value == 0]
            if len(positions) > 1:
                return result
            else:
                result[positions[0]] = math.prod(nums[:positions[0]] + nums[positions[0]+1:])
                return result
        else:
            total = math.prod(nums)
            for i in nums:
                result.append(int(total/i))
        return result