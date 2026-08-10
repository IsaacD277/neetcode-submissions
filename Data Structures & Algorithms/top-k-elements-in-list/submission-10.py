class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            if hashmap.get(i) != None:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
    
        for key, value in hashmap.items():
            buckets[value].append(key)

        final = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                final.append(n)
                if len(final) == k:
                    return final