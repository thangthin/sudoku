__author__ = 'don'

from Tkinter import Tk, RIGHT, BOTH, RAISED, W, E, StringVar
from ttk import Frame, Button, Style, Entry


class Main(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.style = Style()
        self.style.theme_use("clam")
        self.parent = parent
        self.parent.title("Sudoku Solver")
        self.pack(fill=BOTH, expand=1)
        self.square = []
        self.game_size = 3

        self.parent = parent
        self.center_window()
        self.init_ui()

    def center_window(self):
        w = 500
        h = 500

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def init_ui(self):

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)

        for i in range(self.game_size ** 2):
            self.square.append([])
            for j in range(self.game_size ** 2):
                self.square[i].append(StringVar())
                self.square[i][j].trace("w", lambda name, index, mode,
                                        sv=self.square[i][j]: callback(sv))

        for i in range(self.game_size ** 2):
            for j in range(self.game_size ** 2):
                Entry(frame, width=2, justify=RIGHT,
                      textvariable=self.square[i][j]).grid(row=i, column=j)

        quit_button = Button(self, text="Solve",
                             command=self.quit)
        quit_button.pack(side=RIGHT, padx=5, pady=5)

        self.pack()


def callback(sv):
    if len(sv.get()) > 0:
        c = sv.get()[0:1]
        if (ord(c) < 58) & (ord(c) > 48):
            sv.set(c)
        else:
            sv.set("")


def main():
    root = Tk()

    app = Main(root)
    root.mainloop()


if __name__ == '__main__':
    main()


