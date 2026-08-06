class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if nums[i] in lookup:
                j = lookup[nums[i]]
                return [i if i < j else j, i if i > j else j]
            if j in lookup and lookup[j] != i:
                return [i, j]
            else:
                lookup[j] = i