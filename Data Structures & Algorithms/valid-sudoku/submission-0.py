class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            hashset_row = set()
            hashset_col = set()
            for j in range(len(board[i])):
                num = board[i][j]
                if num != '.' and num not in hashset_row:
                    hashset_row.add(num)
                elif num in hashset_row:
                    return False
                
                # Now for the col
                num = board[j][i]
                if num != '.' and num not in hashset_col:
                    hashset_col.add(num)
                elif num in hashset_col:
                    return False

        hashmap = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                x = i//3
                y = j//3
                if (x,y) not in hashmap:
                    hashmap[(x,y)] = set()
                    if board[i][j] != '.':
                        hashmap[(x,y)].add(board[i][j])
                else:
                    num = board[i][j]
                    if num in hashmap[(x,y)]:
                        return False
                    elif num not in hashmap[(x,y)] and num != '.':
                        hashmap[(x,y)].add(num)
        return True
                