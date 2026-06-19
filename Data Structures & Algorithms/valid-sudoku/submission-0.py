class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        column = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if r not in rows:
                    rows[r] = set()
                
                if c not in column:
                    column[c] = set()

                box = (r//3,c//3)

                if box not in boxes:
                    boxes[box] = set()

                if(num in rows[r] or num in column[c] or num in boxes[box]):
                    return False

                rows[r].add(num)
                column[c].add(num)
                boxes[box].add(num)

        return True

        

        