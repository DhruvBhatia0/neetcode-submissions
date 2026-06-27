class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # get full prod
        full_prod = 1
        num_zeros = 0
        for val in nums:
            if val != 0:
                full_prod *= val
            else:
                num_zeros += 1
        
        new_array = []
        for idx, val in enumerate(nums):
            if num_zeros > 0 and val != 0:
                new_array.append(0)
            elif val == 0 and num_zeros == 1:
                new_array.append(full_prod)
            elif val == 0 and num_zeros > 1:
                new_array.append(0)
            else:
                new_array.append(int(full_prod/val))
        
        return new_array

        