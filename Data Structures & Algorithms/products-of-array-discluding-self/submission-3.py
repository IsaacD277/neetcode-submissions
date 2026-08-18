class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)
        res = [0] * count
        left = [0] * count
        right = [0] * count

        left[0] = 1
        right[-1] = 1
        for i in range(1, count):
            left[i] = nums[i-1]*left[i-1]
            # print("Left", i, left)
        for i in range(count-2, -1, -1):
            right[i] = nums[i+1]*right[i+1]
            # print("Righy", i, right)
        for i in range(0,count):
            res[i] = left[i]*right[i]
        
        # print(left)
        # print(right)
        # print(res)

        return res