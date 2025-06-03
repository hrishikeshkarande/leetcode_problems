class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)

        result = []

        for i in range(0,len(candies)):
            if extraCandies + candies[i] >= maxcandies:
                result.append(True) #append function adds further and further to a list/array in python
            else:
                result.append(False)
        return result