class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        Map<Character,Character> cto = new HashMap<>();
        cto.put(')','(');
        cto.put(']','[');
        cto.put('}','{');

        for (char c:s.toCharArray()){
            if (cto.containsKey(c)){
                if(!stk.isEmpty() && stk.peek()==cto.get(c)){
                    stk.pop();
                }else{
                    return false;
                }
            }else{
                stk.push(c);
            }
        }
        return stk.isEmpty();
    }
}
