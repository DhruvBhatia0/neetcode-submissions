class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freak = {}

        for i in nums:
            if i in freak:
                freak[i] += 1
            else:
                freak[i] = 1
        
        return sorted(freak, key=freak.get, reverse=True)[:k]
        