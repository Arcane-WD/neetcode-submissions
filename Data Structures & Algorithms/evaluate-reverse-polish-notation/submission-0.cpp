class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for(string str:tokens){
            if(str=="+"){
                int a = stk.top();stk.pop();
                int b = stk.top();stk.pop();
                stk.push(b+a);
            }else if(str=="-"){
                int a = stk.top();stk.pop();
                int b = stk.top();stk.pop();
                stk.push(b-a);
            }else if(str=="/"){
                int a = stk.top();stk.pop();
                int b = stk.top();stk.pop();
                stk.push(b/a);
            }else if(str=="*"){
                int a = stk.top();stk.pop();
                int b = stk.top();stk.pop();
                stk.push(b*a);
            }else{
                stk.push(stoi(str));
            }
        }
        return stk.top();
    }
};
