import pygame
import sys
from gui import GUI
from algorithm import NQueensDFS

def main():
    app_gui = GUI(n=8)
    app_algo = NQueensDFS(n=8)
    
    current_solution_index = -1
    
    app_gui.render_state(app_algo.board)
    app_gui.draw_status("Hãy đặt 1 quân!", (0, 0, 0))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
                # BẤM: Giải
                if app_gui.btn_solve.collidepoint(x, y):
                    if app_algo.fixed_row != -1: 
                        app_algo.solve_all()
                        if app_algo.solutions:
                            current_solution_index = 0
                            app_gui.render_state(app_algo.solutions[current_solution_index])
                            app_gui.draw_status(f"KQ: 1 / {len(app_algo.solutions)}")
                        else:
                            app_gui.draw_status("Vô nghiệm!", (255, 0, 0))
                            
                # BẤM: < (Kết quả trước)
                elif app_gui.btn_prev.collidepoint(x, y):
                    if app_algo.solutions and current_solution_index > 0:
                        current_solution_index -= 1
                        app_gui.render_state(app_algo.solutions[current_solution_index])
                        app_gui.draw_status(f"KQ: {current_solution_index + 1} / {len(app_algo.solutions)}")
                        
                # BẤM: > (Kết quả tiếp theo)
                elif app_gui.btn_next.collidepoint(x, y):
                    if app_algo.solutions and current_solution_index < len(app_algo.solutions) - 1:
                        current_solution_index += 1
                        app_gui.render_state(app_algo.solutions[current_solution_index])
                        app_gui.draw_status(f"KQ: {current_solution_index + 1} / {len(app_algo.solutions)}")

                # BẤM: Xem quá trình (Animation)
                elif app_gui.btn_play.collidepoint(x, y):
                    if app_algo.solutions and current_solution_index != -1:
                        history_segment = app_algo.get_history_for_solution(current_solution_index)
                        app_gui.draw_status("Đang diễn...", (200, 100, 0))
                        
                        for state in history_segment:
                            # Chống treo cửa sổ (Not Responding) trong lúc animation chạy
                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                    
                            app_gui.render_state(state)
                            pygame.time.delay(50) # Thay đổi tốc độ tại đây (120ms = Vừa phải)
                            
                        app_gui.draw_status(f"KQ: {current_solution_index + 1} / {len(app_algo.solutions)}")

                # BẤM: Xóa bàn cờ
                elif app_gui.btn_reset.collidepoint(x, y):
                    app_algo.reset_board()
                    current_solution_index = -1
                    app_gui.render_state(app_algo.board)
                    app_gui.draw_status("Đã làm mới", (0, 0, 0))
                    
                # BẤM: Đặt quân Hậu đầu tiên lên bàn cờ
                elif x < app_gui.N * app_gui.GRID_SIZE and y < app_gui.N * app_gui.GRID_SIZE:
                    if app_algo.fixed_row == -1:
                        col = x // app_gui.GRID_SIZE
                        row = y // app_gui.GRID_SIZE
                        app_algo.set_fixed_queen(row, col)
                        app_gui.render_state(app_algo.board)
                        app_gui.draw_status("Sẵn sàng giải", (0, 100, 200))

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()