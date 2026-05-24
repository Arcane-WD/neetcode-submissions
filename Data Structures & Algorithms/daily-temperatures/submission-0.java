class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stk = new Stack<>();
        for(int i=0; i<temperatures.length; i++){
            while(!stk.isEmpty() && temperatures[stk.peek()] < temperatures[i]){
                int ind = stk.pop();
                temperatures[ind] = i-ind;
            }
            stk.push(i);
        }
        while (!stk.isEmpty()){
            int ind = stk.pop();
            temperatures[ind]=0;
        }
        return temperatures;
    }
}
