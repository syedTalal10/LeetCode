class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevHap = {}


        for i , n in enumerate(nums):
            difference = target - n
            if difference in prevHap:
                return [prevHap[difference], i]

            else:
                prevHap[n]= i

        return


