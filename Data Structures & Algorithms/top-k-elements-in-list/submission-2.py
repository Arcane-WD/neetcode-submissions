class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = dict()
        for i in nums:
            if i not in dct:
                dct[i] = 0
            dct[i]+=1
        lists = [[] for _ in range(max(dct.values()))]
        for key,v in dct.items():
            lists[v-1].append(key)
        ans = []
        # print(lists)
        for i in range(len(lists)-1, -1, -1):
            if len(lists[i])!=0 and k>0:
                # print(k, lists[i])
                while k>0 and len(lists[i])>0:
                    k-=1
                    ans.append(lists[i].pop())
                
        return ans