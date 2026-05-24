class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for word in strs:
            sword = " ".join(sorted(list(word)))
            if sword not in hashmap:
                hashmap[sword] = []
            hashmap[sword].append(word)
        return list(hashmap.values())