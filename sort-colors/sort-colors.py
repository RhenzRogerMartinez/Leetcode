class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            mid_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[mid_index]:
                    mid_index = j
                    
            nums[mid_index], nums[i] = nums[i], nums[mid_index]