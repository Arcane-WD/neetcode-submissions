class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> myset;
        for(int i:nums){
            if(myset.count(i)){
                return true;
            }else{
                myset.insert(i);
            }
        }
        return false;
    }
};
