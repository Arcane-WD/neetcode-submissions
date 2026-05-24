class Solution {
public:
    bool isAnagram(string s, string t) {
        int a[26]={0};
        for(char c:s){
            a[c-'a']++;
        }
        for(char c:t){
            a[c-'a']--;
        }
        int sum=0;
        for(int i: a){
            sum+=abs(i);
        }
        if(sum==0) return true;
        return false;
    }
};
