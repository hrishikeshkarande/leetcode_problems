class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        p1=0
        while p1<len(nums):
            rem=target-nums[p1]
            if rem in hashmap:
                return [hashmap[rem],p1]
            else:
                hashmap[nums[p1]]=p1
                p1+=1