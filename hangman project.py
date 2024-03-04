import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 20), width=8, height=4,
                                              command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.toggle_player()

    def check_winner(self, row, col):
        # Check row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
            return True
        # Check column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
            return True
        # Check diagonals
        if row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_tie(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
