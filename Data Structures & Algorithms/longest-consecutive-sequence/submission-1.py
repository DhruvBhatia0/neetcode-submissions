class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
            
        starting = {}
        for num in nums:
            if num - 1 not in nums:
                starting[num] = 1
        
        if len(starting.keys()) == len(nums):
            return 1
        
        for num in starting:
            curr_num = num
            while curr_num+1 in nums:
                starting[num] += 1
                curr_num += 1
        
        return sorted(starting.values(), reverse=True)[0]
        
