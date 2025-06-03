class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)

        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            cont_width = right - left
            cont_height = min(height[left],height[right])
            current_area = cont_height * cont_width

            if current_area > max_area:
                max_area = current_area

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_area         