class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> ans;
        for(int i=0;i<nums.size()-2;i++){
            if(i>0&&nums[i]==nums[i-1]) continue;
            int l=i+1,r=nums.size()-1;
            int target = -nums[i]; 
            while(l<r){
                int sum=nums[l]+nums[r];
                if(sum<target){
                    l++;
                }else if(sum>target){
                    r--;
                }else{
                    ans.push_back({nums[i],nums[l],nums[r]});
                    while(l<r&&nums[l]==nums[l+1]) l++;
                    while(l<r&& nums[r]==nums[r-1])r--;
                    l++;
                    r--;
                }
            }
        }
        return ans;
    }
};
