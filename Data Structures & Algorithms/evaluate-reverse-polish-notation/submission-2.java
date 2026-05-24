class Solution {
    public int evalRPN(String[] tokens) {
        List<String> ops = Arrays.asList("+","-","/","*");
        Stack<String> stk = new Stack<>();
        for (String ch:tokens){
            System.out.println(stk);
            if (!ops.contains(ch)){
                stk.push(ch);
            }else{
                int b = Integer.parseInt(stk.pop());
                int a = Integer.parseInt(stk.pop());
                if (ch.equals("+")){
                    stk.push(Integer.toString(a+b));
                }else if(ch.equals("-")){
                    stk.push(Integer.toString(a-b));
                }else if(ch.equals("*")){
                    stk.push(Integer.toString(a*b));
                }else if(ch.equals("/")){
                    stk.push(Integer.toString(a/b));
                }
            }
        }
        return Integer.parseInt(stk.pop());
    }
}
