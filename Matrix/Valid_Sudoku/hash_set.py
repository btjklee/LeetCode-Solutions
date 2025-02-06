# ✅ Valid Sudoku - Python Solution
# 🔗 Problem Link: https://leetcode.com/problems/valid-sudoku/

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9  # Standard Sudoku board size

        # Use hash sets to track numbers seen in each row, column, and box
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        # Iterate through the board
        for r in range(N):
            for c in range(N):
                val = board[r][c]

                # Ignore empty cells
                if val == ".":
                    continue

                # Check row constraint
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check column constraint
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check 3×3 box constraint
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True  # If no violations, the board is valid
