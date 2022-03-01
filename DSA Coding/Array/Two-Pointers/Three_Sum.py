#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                low = i + 1
                high = len(nums) - 1
                sum = 0 - nums[i]
                while (low < high):
                    if nums[low] + nums[high] == sum:
                        res.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < sum:
                        low += 1
                    else:
                        high -= 1
        return res
                        
                
           