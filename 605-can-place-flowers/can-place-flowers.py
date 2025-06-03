class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0 # How many flowers we have planted so far
        length = len(flowerbed)

        if n == 0:
            return True #Because if n=0, we don’t even need to plant — the answer is trivially True!


        for i in range(length):
            # Check if current plot is empty
            if flowerbed[i] == 0:
                # Check left neighbor (or treat as empty if at start)
                left = (i == 0) or (flowerbed[i-1] == 0)
                # Check right neighbor (or treat as empty if at end)
                right = (i == length-1) or (flowerbed[i+1] == 0)
                
                # If both neighbors are empty, plant a flowe
                if left and right:
                    flowerbed[i] = 1 # Plant flower
                    count = count + 1
                    if count >= n:
                        return True # Enough flowers planted
        return False
