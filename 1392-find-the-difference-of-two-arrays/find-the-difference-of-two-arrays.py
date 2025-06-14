class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        mySet1 = set(nums1)
        mySet2 = set(nums2)

        diff1 = mySet1 - mySet2
        diff2 = mySet2 - mySet1

        return[list(diff1),list(diff2)]
         