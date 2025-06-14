class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #Sets do not have duplicate values, so will convert both the lists to sets

        mySet1 = set(nums1)
        mySet2 = set(nums2)

        #Now we will take the difference of the two sets and store them in two variables called diff1 and diff2

        diff1 = mySet1 - mySet2
        diff2 = mySet2 - mySet1

        #Return the two difference sets after converting them to lists because the output is required in lists
        return[list(diff1),list(diff2)]
         