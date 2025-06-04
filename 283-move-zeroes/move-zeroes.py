class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        \U0001f50d Explanation
        We shift all non-zero elements forward using slow.
        When done, we fill the rest of the array with 0s.

        """
        length = len(nums)
        # Pointer to track the next position for a non-zero element
        slow = 0

        # First pass: move non-zero elements to the front
        for fast in range(0, length):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1 # Increment to next empty spot
        
        # Second pass: fill the remaining positions with zeros
        for i in range(slow, length):
            nums[i]=0

