class Solution {
    public int[] productExceptSelf(int[] nums) {
        int zeros=0;
        int product = 1;
        for(int num:nums){
            if (num==0){
                zeros++;
            }else{
                product*=num;
            }
        }
        int[] res = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=0){
                if (zeros>0){
                    res[i]=0;
                }else{
                    res[i]=product/nums[i];
                }
            }else{
                if(zeros>1){
                    res[i]=0;
                }else{
                    res[i]=product;
                }
            }
        }
        return res;
    }
}  
