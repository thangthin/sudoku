__author__ = 'don'
import itertools
import ExactCover

#provide chain functions (takes list of lists and concatenates

#
def list_repeats(subset):
    return list(set([x for x in subset if subset.count(x) > 1]))


def list_invalids(subset):
    invalid_char = []
    for c in subset:
        if (ord(c) > 57) | (ord(c) < 49):
            invalid_char.append(c)
    return invalid_char


def column(self, i):
    return [row[i] for row in self.puzzle]


def block(self, i):
    sub_row = (i%self.size)*self.size
    sub_col = (i/self.size)*self.size
    return ''.join([row[sub_row:sub_row+self.size] for row in
           self.puzzle[sub_col:sub_col+3]])


def check_matrix(self):
    row_repeats = []
    col_repeats = []
    block_repeats = []
    row_invalids = []

    for i in range(len(self.puzzle)):
        row_invalids.append(list_invalids(self.puzzle[i]))
        row_repeats.append(list_repeats(self.puzzle[i]))
        col_repeats.append(list_repeats(column(self, i)))
        block_repeats.append(list_repeats(block(self, i)))

    if len(list(itertools.chain(*row_invalids))) > 0:
        print "invalids: "
        print row_invalids
        return False

    if len(list(itertools.chain(*row_repeats))) > 0:
        print "row_repeats: "
        print row_repeats
        return False

    if len(list(itertools.chain(*col_repeats))) > 0:
        print "col_repeats: "
        print col_repeats
        return False

    if len(list(itertools.chain(*block_repeats))) > 0:
        print "block_repeats"
        print block_repeats
        return False

    return True


# create a sparse matrix for the constraints of the sudoku puzzle
# size is dependent on the size of puzzle


