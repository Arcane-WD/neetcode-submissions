class MinStack {
public:
    vector<int> stk;
    MinStack() {
        
    }
    
    void push(int val) {
        stk.push_back(val);
    }
    
    void pop() {
        stk.pop_back();
    }
    
    int top() {
        return stk[stk.size()-1];
    }
    
    int getMin() {
        return *min_element(stk.begin(),stk.end());
    }
};
