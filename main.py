import tkinter as tk
from gui import SudokuSolverGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
