__author__ = 'thang'

from Tkinter import * # Import tkinter

puzzle_list = []
puzzle_string_list = []
solved_puzzle = ["417523698","253986147","986174325","691857432","532469871",
                 "748231569","379615284","865742913","124398756"]

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

        self.dlxButton = Button(self.myContainer3, text = "DLX",
                                      command=self.dlx_solve).pack(side=LEFT)

        self.satButton = Button(self.myContainer3, text = "SAT",
                                      command=self.sat_solve).pack(side=LEFT)

        self.quitButton = Button(self.myContainer3, text = "Quit Program",
                                 command=self.quit_game).pack(side=LEFT)

        self.testButton = Button(self.myContainer3, text = "test",
                                 command=self.puzzle_print).pack(side=LEFT)
        self.clearButton = Button(self.myContainer3, text = "Clear",
                                  command=self.clear_screen).pack(side=LEFT)

### Parse to convert it to required list type
    def write_gui(self):
        r = 0
        for col in self.rows:
            c = 0
            for e in col:
                e.delete(0, END)
                e.insert(0, solved_puzzle[r][c])
                c += 1
            r += 1

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

    def dlx_solve(self):
        print "solve with dlx code"
        print self.rows
        self.write_gui()
        # r = 0
        # for col in self.rows:
        #     c = 0
        #     for e in col:
        #         e.delete(0, END)
        #         e.insert(0, solved_puzzle[r][c])
        #         c += 1
        #     r += 1


    def sat_solve(self):
        print "solve with sat code"
        self.write_gui()

    def quit_game(self):
        self.myParent.destroy()

    def puzzle_print(self):
        print(puzzle_list)
        print(puzzle_string_list)

    def clear_screen(self):
        for col in self.rows:
            for e in col:
                e.delete(0, END)
        del puzzle_list[:]
        del puzzle_string_list[:]




root = Tk()
sudoku_gui = Sudoku_UI(root)
root.mainloop()