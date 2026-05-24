class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int row=0; row<9;row++){
            Set<Character> seen = new HashSet<>();
            for(int col=0;col<9;col++){
                if (board[row][col]=='.') continue;
                if (seen.contains(board[row][col])) return false;
                seen.add(board[row][col]);
            }
        }
        for (int row=0; row<9;row++){
            Set<Character> seen = new HashSet<>();
            for(int col=0;col<9;col++){
                if (board[col][row]=='.') continue;
                if (seen.contains(board[col][row])) return false;
                seen.add(board[col][row]);
            }
        }

        for (int sq=0; sq<9;sq++){
            Set<Character> seen = new HashSet<>();
            for (int i=0; i<3;i++){
                for (int j=0;j<3;j++){
                    int row = (sq/3)*3 + i;
                    int col = (sq%3) * 3 + j;
                    if(board[row][col]=='.') continue;
                    if(seen.contains(board[row][col])) return false;
                    seen.add(board[row][col]);
                }
            }
        }
        return true;
    }
}
