class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Initialize the current altitude at the starting point (0)
        current_altitude = 0
        # Initialize the maximum altitude also at 0 (start point)
        max_altitude = 0

        # Iterate over each element in gain to track the altitude changes
        for i in range(len(gain)):
             # Update the current altitude by adding the net gain at this step
            current_altitude = current_altitude + gain[i]

            # If the current altitude is higher than the max so far, update max_altitude
            if current_altitude > max_altitude:
                max_altitude = current_altitude

        # After processing all the gains, max_altitude holds the highest altitude reached
        return max_altitude