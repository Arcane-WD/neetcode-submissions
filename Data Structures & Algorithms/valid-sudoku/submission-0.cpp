class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
    return rowCheck(board) && colCheck(board) && boxCheck(board);
}


    bool boxCheck(vector<vector<char>>& board) {
    for (int boxRow = 0; boxRow < 3; ++boxRow) {
        for (int boxCol = 0; boxCol < 3; ++boxCol) {
            unordered_set<char> box;
            for (int i = 0; i < 3; ++i) {
                for (int j = 0; j < 3; ++j) {
                    char val = board[boxRow * 3 + i][boxCol * 3 + j];
                    if (val != '.') {
                        if (box.count(val)) {
                            return false;
                        } else {
                            box.insert(val);
                        }
                    }
                }
            }
        }
    }
    return true;
}


    bool rowCheck(vector<vector<char>>& board){
        for(int i=0; i<9;i++){
            unordered_set<int> row;
            for(int j=0;j<9;j++){
                if(board[i][j]!='.'){
                    if(row.count(board[i][j])){
                        return false;
                    }else{
                        row.insert(board[i][j]);
                    }
                }
            }
        }
        return true;
    }

    bool colCheck(vector<vector<char>>& board){
        for(int i=0; i<9;i++){
            unordered_set<int> col;
            for(int j=0;j<9;j++){
                if(board[j][i]!='.'){
                    if(col.count(board[j][i])){
                        return false;
                    }else{
                        col.insert(board[j][i]);
                    }
                }
            }
        }
        return true;
    }
};
