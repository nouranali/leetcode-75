class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=str(int(''.join(str(i)for i in digits)) +1)
        return [i for i in n]
