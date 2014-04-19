__author__ = 'don'
import Sudoku

class Main():
    def __init__(self, parent):
        self.matrix = []
        self.size = 3
        self.file = open("test/problem1.txt")

    def main(self):
        for line in self.file:
            self.matrix.append(line[0:9])

        for row in self.matrix:
            print row

        Sudoku.check_matrix(self)



if __name__ == '__main__':
    Main(object).main()