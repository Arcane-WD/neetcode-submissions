class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int> vleft(n);
        vector<int> vright(n);
        vector<int> res(n);

        vleft[0]=1;
        vright[n-1]=1;
        for(int i=1;i<n;i++){
            vleft[i]=nums[i-1]*vleft[i-1];
        }
        for(int i=n-2;i>=0;i--){
            vright[i] = vright[i+1]*nums[i+1];
        }
        for(int i=0;i<n;i++){
            res[i] = vleft[i]*vright[i];
        }
        return res;
    }
};
