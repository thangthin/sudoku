__author__ = 'don'
import Sudoku
import ExactCover
import SatSolver


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

class Main():
    def __init__(self, parent):
        self.puzzle = []
        self.size = 3
        self.file = open("test/problem1.txt")
        self.converted = []

    def main(self):
        for line in self.file:
            char_list = []
            for c in line[0:9]:
                char_list.append(c)
            self.puzzle.append(char_list)

        dlx = DLX(self.puzzle)
        if dlx.solve():
            self.puzzle = dlx.get_puzzle()
            self.str_list = []
            for m in self.puzzle:
                print "".join(m)
                self.str_list.append("".join(m))

            self.puzzle = self.str_list
            if Sudoku.check_matrix(self):
                print "solved"
        else:
            print "not a valid puzzle"






if __name__ == '__main__':
    Main(object).main()