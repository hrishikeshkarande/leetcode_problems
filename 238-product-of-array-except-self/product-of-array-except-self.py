from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an array of integers `nums`, this function returns an array `answer` such that:
            answer[i] = product of all elements in nums except nums[i],
        without using division, and in O(n) time.

        We do this by calculating:
        1. A prefix product for each index (product of all elements to the *left* of i)
        2. A suffix product for each index (product of all elements to the *right* of i)
        Then we multiply them for each index.

        Example:
        nums = [1, 2, 3, 4]

        Prefix pass:
        i=0 → answer[0] = 1 (initial), prefix = 1 * 1 = 1
        i=1 → answer[1] = 1, prefix = 1 * 2 = 2
        i=2 → answer[2] = 2, prefix = 2 * 3 = 6
        i=3 → answer[3] = 6, prefix = 6 * 4 = 24
        Result after prefix pass: answer = [1, 1, 2, 6]

        Suffix pass:
        i=3 → answer[3] *= 1 → 6, suffix = 1 * 4 = 4
        i=2 → answer[2] *= 4 → 8, suffix = 4 * 3 = 12
        i=1 → answer[1] *= 12 → 12, suffix = 12 * 2 = 24
        i=0 → answer[0] *= 24 → 24, suffix = 24 * 1 = 24
        Final result: answer = [24, 12, 8, 6]
        """

        # Initialize the answer array with 1s.
        # This will be used to store prefix products initially,
        # and later combined with suffix products.
        answer = [1] * len(nums)

        # prefix holds the product of all elements to the left of current index
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix      # Set current answer[i] to product of elements before index i
            prefix *= nums[i]       # Update prefix to include nums[i] for next iteration

        # suffix holds the product of all elements to the right of current index
        suffix = 1
        for i in range(len(nums)-1, -1, -1):  # iterate from last index to 0
            answer[i] *= suffix      # Multiply with product of elements after index i
            suffix *= nums[i]        # Update suffix to include nums[i] for next iteration

        return answer
