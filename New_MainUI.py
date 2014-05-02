__author__ = 'thang'

from Tkinter import * # Import tkinter

puzzle_list = []
puzzle_string_list = []

class Sudoku_UI:
    #puzzle_list = []
    #puzzle_string_list = []

    def __init__(self,parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myParent.title("Sudoku Solver GUI")
        self.myContainer1.pack()

        self.myContainer2 = Frame(self.myContainer1)
        self.myContainer2.pack()
        self.rows = []
        self.grey_row = [0,1,2,6,7,8]
        self.grey_col = [0,1,2,6,7,8]
        self.center_box = [3,4,5]
        for i in range(9):
            cols = []
            for j in range(9):
                if (i in self.grey_row) and (j in self.grey_col):
                    e = Entry(self.myContainer2, width=4, relief=RIDGE,
                              bg = "grey")
                elif (i in self.center_box) and (j in self.center_box):
                    e = Entry(self.myContainer2, width=4, relief=RIDGE,
                              bg = "grey")
                else:
                    e = Entry(self.myContainer2, width=4, relief=RIDGE,
                              bg = "white")
                e.grid(row=i, column = j, sticky = NSEW)
                cols.append(e)
            self.rows.append(cols)

        self.myContainer3 = Frame(self.myContainer1)
        self.myContainer3.pack()

        self.submitButton = Button(self.myContainer3, text = "Submit",
                                  command=self.submit).pack(side=LEFT)

        self.newPuzzleButton = Button(self.myContainer3, text = "New Puzzle",
                                      command=self.new_puzzle).pack(side=LEFT)

        self.quitButton = Button(self.myContainer3, text = "Quit Program",
                                 command=self.quit_game).pack(side=LEFT)

        self.testButton = Button(self.myContainer3, text = "test",
                                 command=self.puzzle_print).pack(side=LEFT)

### Parse to convert it to required list type
    def submit(self):
        for row in self.rows:
            cols = []
            for col in row:
                cols.append(col.get())
            puzzle_list.append(cols)
            i = 0
            for e in cols:
                if e == '':
                    cols[i] = '0'
                i += 1

            puzzle_string_list.append(''.join(cols))


    def new_puzzle(self):
        print "new game code"

    def quit_game(self):
        self.myParent.destroy()

    def puzzle_print(self):
        print(puzzle_list)
        print(puzzle_string_list)




root = Tk()
sudoku_gui = Sudoku_UI(root)
root.mainloop()