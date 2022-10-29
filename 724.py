class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        left=0
        for i,n in enumerate(nums):
            if s-n-left == left:
                return i
            left+=n
        return -1
            
        