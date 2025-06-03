class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Step 1: Calculate the sum of the first window of size k
        current_sum = sum(nums[0:k])

        max_sum = current_sum  # Initialize max_sum with the sum of the first window

        # Step 2: Slide the window through the array
        for i in range (k, len(nums)):

            # Subtract the element that leaves the window
            current_sum = current_sum - nums[i - k]

            # Add the new element that enters the window
            current_sum = current_sum + nums[i]

            # Update max_sum if we have a new maximum
            if current_sum > max_sum:
                max_sum = current_sum
        
        # Step 3: Compute and return the maximum average
        max_average = max_sum / k
        return max_average
        

'''

\U0001f4a1 Let’s break it down:
✅ current_sum
The sum of the current window.

✅ Initial sum
We use sum(nums[:k]) to get the sum of the first window.

✅ Sliding the window
In each iteration:

We remove the element at i - k (because it’s no longer in the window).

We add the new element at i (because it’s the new element in the window).

We update max_sum if this new sum is larger.

✅ Final average
Finally, divide max_sum by k to get the maximum average.

'''