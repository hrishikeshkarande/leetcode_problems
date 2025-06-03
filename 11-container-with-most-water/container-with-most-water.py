class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Number of vertical lines
        n = len(height)

        # Initialize two pointers:
        # - 'left' starts at the beginning (0 index)
        # - 'right' starts at the end (last index)
        left = 0
        right = n - 1

        # Initialize variable to track the maximum area found
        max_area = 0

        # Continue while the two pointers have not crossed
        while left < right:
            # Calculate the width of the container between the two lines
            cont_width = right - left

            # Determine the height of the container (minimum of the two lines)
            cont_height = min(height[left], height[right])

            # Calculate the current area
            current_area = cont_height * cont_width

            # Update max_area if the current area is larger
            if current_area > max_area:
                max_area = current_area

            # Move the pointer at the shorter line inward to try and find a taller line
            # - this might help to increase the area in the next iteration
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        # After checking all possible pairs, max_area will hold the largest container area
        return max_area
