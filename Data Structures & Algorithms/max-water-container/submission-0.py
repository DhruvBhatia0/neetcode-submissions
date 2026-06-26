class Solution:

    def area (self, heights, lp, rp):
        return (rp - lp) * min(heights[lp], heights[rp])

    def maxArea(self, heights: List[int]) -> int:

        lp = 0
        rp = len(heights) - 1

        curr_max = 0

        while lp != rp:
            curr_max = max(curr_max, self.area(heights, lp, rp))

            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
        
        return curr_max



        