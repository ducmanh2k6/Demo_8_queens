import pygame

class GUI:
    def __init__(self, n=8):
        pygame.init()
        self.N = n
        self.GRID_SIZE = 50
        
        # Kích thước bàn cờ
        board_width = self.GRID_SIZE * self.N
        board_height = self.GRID_SIZE * self.N
        
        # Mở rộng cửa sổ sang phải thêm 160 pixel để làm cột chứa nút
        self.PANEL_WIDTH = 160
        self.width = board_width + self.PANEL_WIDTH
        self.height = board_height
        
        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption('Giải bài toán 8 quân hậu')
        
        self.LIGHT_COLOR = (255, 206, 158)
        self.DARK_COLOR = (209, 139, 71)
        
        self.font = pygame.font.SysFont("tahoma", 13, bold=True) 
        
        queen_img_raw = pygame.image.load('./images/queen.png')
        self.queen_img = pygame.transform.scale(queen_img_raw, (self.GRID_SIZE, self.GRID_SIZE))
        
        # --- ĐỊNH NGHĨA VỊ TRÍ CÁC NÚT DỌC BÊN PHẢI ---
        # Tọa độ X chung cho các nút (cách mép phải bàn cờ 15 pixel)
        x_btn = board_width + 15
        btn_width = 130
        btn_height = 40
        spacing = 15 # Khoảng cách dọc giữa các nút
        
        start_y = 20
        self.btn_solve = pygame.Rect(x_btn, start_y, btn_width, btn_height)
        
        # Nút < và > có thể để chung một dòng cho gọn
        half_w = (btn_width - 10) // 2
        self.btn_prev  = pygame.Rect(x_btn, start_y + (btn_height + spacing), half_w, btn_height)
        self.btn_next  = pygame.Rect(x_btn + half_w + 10, start_y + (btn_height + spacing), half_w, btn_height)
        
        self.btn_play  = pygame.Rect(x_btn, start_y + (btn_height + spacing) * 2, btn_width, btn_height)
        self.btn_reset = pygame.Rect(x_btn, start_y + (btn_height + spacing) * 3, btn_width, btn_height)

    def draw_empty_grid(self):
        # Vẽ bàn cờ
        for row in range(self.N):
            for col in range(self.N):
                color = self.LIGHT_COLOR if (row + col) % 2 == 0 else self.DARK_COLOR
                pygame.draw.rect(self.screen, color, 
                                 (col * self.GRID_SIZE, row * self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))
                                 
        # Vẽ phần nền xám bên phải cho bảng điều khiển nút bấm
        panel_rect = pygame.Rect(self.N * self.GRID_SIZE, 0, self.PANEL_WIDTH, self.height)
        pygame.draw.rect(self.screen, (240, 240, 240), panel_rect)
        
        # Kẻ đường viền ngăn cách giữa bàn cờ và bảng điều khiển
        pygame.draw.line(self.screen, (200, 200, 200), (self.N * self.GRID_SIZE, 0), (self.N * self.GRID_SIZE, self.height), 2)
        
        self.draw_buttons()

    def draw_buttons(self):
        # Nút Giải
        pygame.draw.rect(self.screen, (65, 105, 225), self.btn_solve, border_radius=5)
        self.screen.blit(self.font.render("Giải", True, (255, 255, 255)), (self.btn_solve.x + 48, self.btn_solve.y + 11))

        # Nút <
        pygame.draw.rect(self.screen, (169, 169, 169), self.btn_prev, border_radius=5)
        self.screen.blit(self.font.render("<", True, (255, 255, 255)), (self.btn_prev.x + 23, self.btn_prev.y + 11))

        # Nút >
        pygame.draw.rect(self.screen, (169, 169, 169), self.btn_next, border_radius=5)
        self.screen.blit(self.font.render(">", True, (255, 255, 255)), (self.btn_next.x + 23, self.btn_next.y + 11))

        # Nút Xem bước giải
        pygame.draw.rect(self.screen, (46, 139, 87), self.btn_play, border_radius=5)
        self.screen.blit(self.font.render("Xem bước giải", True, (255, 255, 255)), (self.btn_play.x + 18, self.btn_play.y + 11))

        # Nút Xóa / Dọn
        pygame.draw.rect(self.screen, (220, 20, 60), self.btn_reset, border_radius=5)
        self.screen.blit(self.font.render("Dọn bàn cờ", True, (255, 255, 255)), (self.btn_reset.x + 28, self.btn_reset.y + 11))

    def render_state(self, board_state):
        self.draw_empty_grid()
        for row, col in enumerate(board_state):
            if col != -1:
                self.screen.blit(self.queen_img, (col * self.GRID_SIZE, row * self.GRID_SIZE))
        pygame.display.flip()

    def draw_status(self, text, color=(0, 128, 0)):
        # Vẽ khung hiển thị trạng thái / số thứ tự lời giải ở phía dưới cùng của cột phải
        status_rect = pygame.Rect(self.N * self.GRID_SIZE + 15, self.height - 60, 130, 45)
        pygame.draw.rect(self.screen, (255, 255, 255), status_rect, border_radius=5)
        pygame.draw.rect(self.screen, (200, 200, 200), status_rect, 1, border_radius=5)
        
        status_text = self.font.render(text, True, color)
        self.screen.blit(status_text, (status_rect.x + 10, status_rect.y + 13))
        pygame.display.flip()