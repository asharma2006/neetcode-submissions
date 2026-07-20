class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # given 9 x 9
        # each row must have digits 1-9
        # each column must have digits 1-9
        # each 3x3 sub boxes much contain the degits 1-9 without dupes
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # this is r // 3, c // 3

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in rows[r]
                    or board[r][c] in columns[c]
                    or board[r][c] in squares[r // 3, c // 3]
                ):
                    return False

                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])

        return True
        