__author__ = 'thang'

from Tkinter import *
import ExactCover
import time


puzzle_list = []
puzzle_string_list = []
solved_puzzle = []

class DLX():
    def __init__(self, puzzle):
        self.rcn = []
        self.puzzle = puzzle
        self.num_of_constraints = 324
        self.matrix = self.create_constraint_lists()
        self.dlx = ExactCover.DancingLink(self.num_of_constraints,
                                          self.matrix)

    def create_constraint_lists(self):
        rows = []
        for r in range(0, 9):
            for c in range(0, 9):
                for n in range(0, 9):
                    constraints = []
                    row_col = (9 * r) + (c)
                    row_num = 81 + (r * 9) + n
                    col_num = (81 * 2) + (c * 9) + n
                    box_num = (81 * 3) + (((c / 3) + ((r / 3) * 3)) * 9) + n
                    constraints.append(row_col)
                    constraints.append(row_num)
                    constraints.append(col_num)
                    constraints.append(box_num)
                    rows.append(constraints)
                    self.rcn.append((r, c, n+1))
        return rows

    def solve(self):
        for r in range (0,9):
            for c in range(0,9):
                if self.puzzle[r][c] != '0':
                    cell = int(self.puzzle[r][c])
                    pos = (81*r) + (9*c) + (cell-1)
                    row_col = (9*r) + c
                    col = self.dlx.sm.headers[row_col+1].down
                    while col != self.dlx.sm.headers[row_col+1]:
                        if col.row == pos:
                            self.dlx.cover(col)
                        col = col.down

        if self.dlx.search():
            for i in self.dlx.solution:
                r, c, n = self.rcn[i.row]
                self.puzzle[r][c] = str(n)
            return True
        else:
            return False

    def get_puzzle(self):
        return self.puzzle

class SAT():
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.clauses = self.create_clauses()
        pass

    def create_clauses(self):
        pass

    def solve(self):
        pass

    def get_puzzle(self):
        return self.puzzle


### Main UI for program
class Sudoku_UI:
    dlx = []
    sat = []
    def __init__(self,parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myParent.title("Sudoku Solver GUI")
        self.myContainer1.pack()
### TIMER WIDGET

### PUZZLE DISPLAY
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
### BUTTONS
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
        # self.testButton = Button(self.myContainer3, text = "test",
        #                          command=self.puzzle_print).pack(side=LEFT)
        self.clearButton = Button(self.myContainer3, text = "Clear",
                                  command=self.clear_screen).pack(side=LEFT)

### Time
    def start_build_timer(self):
        self.start_build = time.time()

    def stop_build_timer(self):
        self.stop_build = time.time()




### Helper
    def write_gui(self):
        r = 0
        for col in self.rows:
            c = 0
            for e in col:
                e.delete(0, END)
                e.insert(0, solved_puzzle[r][c])
                c += 1
            r += 1
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
        self.dlx = DLX(puzzle_list)
        self.sat = SAT(puzzle_list)
        print puzzle_list
        print self.dlx



### Solve puzzle with DLX algorithm
    def dlx_solve(self):
        self.start_build_timer()
        print "solve with dlx code"
        if self.dlx.solve():
            self.stop_build_timer()
           # self.timeDisplay.delete(0, END)
           # self.timeDisplay.insert(0, str(self.start_build - self.stop_build))
            t = str(self.stop_build - self.start_build)
            print "Time it took to solve puzzle " + t
            global puzzle_list
            puzzle_list = self.dlx.get_puzzle()
            global solved_puzzle
            solved_puzzle = self.dlx.get_puzzle()
            self.write_gui()
        else:
            print "Sudoku not solvable"
        print self.rows
        self.write_gui()

### Solve puzzle with SAT algorithm
    def sat_solve(self):
        print "solve with sat code"
        self.write_gui()

    def quit_game(self):
        self.myParent.destroy()

### Clear the gui screen
    def clear_screen(self):
        for col in self.rows:
            for e in col:
                e.delete(0, END)
        del puzzle_list[:]
        del puzzle_string_list[:]

### Temporary helper to print list to console
    def puzzle_print(self):
        print(puzzle_list)
        print(puzzle_string_list)
        print "This is the solved puzzle"
        print(solved_puzzle)


def mainUI():
    root = Tk()
    sudoku_gui = Sudoku_UI(root)
    root.mainloop()

mainUI()
