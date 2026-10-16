class NQueensDFS:
    def __init__(self, n):
        self.N = n
        self.board = [-1] * n  
        self.fixed_row = -1
        self.fixed_col = -1
        self.solutions = []
        self.history = []               # Lưu toàn bộ quá trình đặt/rút quân
        self.solution_milestones = []   # Lưu index (vị trí) của các lời giải trong history

    def set_fixed_queen(self, row, col):
        self.fixed_row = row
        self.fixed_col = col
        self.board[row] = col

    def is_safe(self, row, col):
        for i in range(self.N):
            if i != row and self.board[i] != -1:
                if self.board[i] == col or \
                   self.board[i] - i == col - row or \
                   self.board[i] + i == col + row:
                    return False
        return True

    def dfs(self, depth=0):
        # Khi tìm thấy lời giải
        if depth == self.N:
            self.solutions.append(list(self.board))
            self.history.append(list(self.board))
            self.solution_milestones.append(len(self.history) - 1)
            return False
        
        # Bỏ qua hàng đã được người dùng đặt cố định từ trước
        if depth == self.fixed_row:
            if self.is_safe(depth, self.fixed_col):
                self.dfs(depth + 1)
            return False

        # Thử đặt Hậu vào các cột
        for col in range(self.N):
            if self.is_safe(depth, col):
                self.board[depth] = col
                self.history.append(list(self.board)) # Ghi lại trạng thái đi tới
                
                self.dfs(depth + 1)
                
                # Quay lui (Backtrack)
                self.board[depth] = -1
                self.history.append(list(self.board)) # Ghi lại trạng thái quay lui
                
        return False

    def solve_all(self):
        self.solutions = []
        self.history = []
        self.solution_milestones = []
        
        self.history.append(list(self.board)) # Trạng thái bắt đầu
        self.dfs(0)
        return self.solutions

    def get_history_for_solution(self, index):
        """Trích xuất đoạn lịch sử duyệt DFS dẫn tới lời giải thứ 'index'"""
        if index == 0:
            start = 0
        else:
            # Bắt đầu từ lời giải trước đó
            start = self.solution_milestones[index - 1] 
            
        end = self.solution_milestones[index]
        return self.history[start : end + 1]

    def reset_board(self):
        self.board = [-1] * self.N
        self.fixed_row = -1
        self.fixed_col = -1
        self.solutions = []
        self.history = []
        self.solution_milestones = []