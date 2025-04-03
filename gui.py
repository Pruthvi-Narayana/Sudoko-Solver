import tkinter as tk
from tkinter import messagebox
from solver import solve

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid_entries = []

        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(root, width=3, font=("Arial", 18), justify="center")
                entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            self.grid_entries.append(row_entries)

        solve_button = tk.Button(root, text="Solve", font=("Arial", 14), command=self.solve_sudoku)
        solve_button.grid(row=9, column=3, columnspan=3, pady=10)

    def get_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.grid_entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def display_solution(self, solved_grid):
        for i in range(9):
            for j in range(9):
                self.grid_entries[i][j].delete(0, tk.END)
                self.grid_entries[i][j].insert(0, str(solved_grid[i][j]))

    def solve_sudoku(self):
        grid = self.get_grid()
        solved_grid = solve(grid)

        if solved_grid == -1:
            messagebox.showerror("Error", "This Sudoku puzzle is unsolvable!")
        else:
            self.display_solution(solved_grid)
