class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counter = [0]*26
        for i in range(len(s)):
            counter[ord(s[i])-97]+=1
            counter[ord(t[i])-97]-=1
        return max(counter) == min(counter) == 0