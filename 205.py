# the idea is to check if num of unique values in s = num of unique values in s = num of unique tuples formed from letteres
# of s and t >> s=foo, t=bar s=(f,o) t=(b,a,r) >> False
# s="egg", t="add", s=(e,g), t=(a,d) s,t=(e,a)+(g,d) >> True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(zip(s,t))) == len(set(t))
        