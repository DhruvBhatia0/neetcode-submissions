class Solution:
    def __init__(self):
        self.cache = {}

    def rob(self, nums: List[int]) -> int:

        '''
        in a set of 3, you might only be able to rob 1
        '''
        total = 0

        if str(nums) in self.cache:
            return self.cache[str(nums)]

        # in recent set of 3, pick a stratergy
        if len(nums) == 0:
            return total

        if len(nums) < 2:
            total += max(nums)
            self.cache[str(nums)] = total
            return total

        house1, house2 = nums[:2]

        self.cache[str(nums[2:])] = self.rob(nums[2:])
        self.cache[str(nums[3:])] = self.rob(nums[3:])

        house1_potential = house1 + self.rob(nums[2:])
        house2_potential = house2 + self.rob(nums[3:])

        total += max(house1_potential, house2_potential)

        return total