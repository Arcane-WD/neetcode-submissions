class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num:nums){
            seen.add(num);
        }
        int res=0;
        for (int num:seen){
            if (!seen.contains(num-1)){
                int len = 1;
                while(seen.contains(num+len)){
                    len++;
                }
                res=Math.max(len,res);
            } 
        }
        return res;
    }
}
