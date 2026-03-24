# -------------------------------
# 1. N-Queens Problem
# -------------------------------
def solve_n_queens(n):
    board = [["."] * n for _ in range(n)]
    result = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)
    return result


# -------------------------------
# 2. Sudoku Solver
# -------------------------------
def solve_sudoku(board):
    """
    board: 9x9 grid with '.' for empty
    modifies board in-place
    """

    def is_valid(r, c, val):
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False

        box_r, box_c = (r // 3) * 3, (c // 3) * 3
        for i in range(box_r, box_r + 3):
            for j in range(box_c, box_c + 3):
                if board[i][j] == val:
                    return False

        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for val in map(str, range(1, 10)):
                        if is_valid(r, c, val):
                            board[r][c] = val
                            if backtrack():
                                return True
                            board[r][c] = "."
                    return False
        return True

    backtrack()


# -------------------------------
# 3. Subsets (Power Set)
# -------------------------------
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


# -------------------------------
# 4. Permutations
# -------------------------------
def permutations(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


# -------------------------------
# 5. Combination Sum
# -------------------------------
def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result


# -------------------------------
# 6. Word Search
# -------------------------------
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != word[i]):
            return False

        temp = board[r][c]
        board[r][c] = "#"

        found = (
            dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1)
        )

        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False


# -------------------------------
# 7. Rat in a Maze
# -------------------------------
def rat_in_maze(maze):
    n = len(maze)
    path = []

    def backtrack(r, c, current_path):
        if r == n - 1 and c == n - 1:
            path.append(current_path)
            return

        if r < 0 or c < 0 or r >= n or c >= n or maze[r][c] == 0:
            return

        maze[r][c] = 0  # mark visited

        backtrack(r + 1, c, current_path + "D")
        backtrack(r, c + 1, current_path + "R")
        backtrack(r - 1, c, current_path + "U")
        backtrack(r, c - 1, current_path + "L")

        maze[r][c] = 1  # unmark

    if maze[0][0] == 1:
        backtrack(0, 0, "")

    return path


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    print("N-Queens (4):", solve_n_queens(4))

    sudoku = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    solve_sudoku(sudoku)
    print("Solved Sudoku:", sudoku)

    print("Subsets:", subsets([1, 2, 3]))
    print("Permutations:", permutations([1, 2, 3]))

    print("Combination Sum:", combination_sum([2, 3, 6, 7], 7))

    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    print("Word Search (ABCCED):", exist(board, "ABCCED"))

    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    print("Rat in Maze Paths:", rat_in_maze(maze))
