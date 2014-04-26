__author__ = 'don'
import itertools
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
    return [row[i] for row in self.matrix]


def block(self, i):
    sub_row = (i%self.size)*self.size
    sub_col = (i/self.size)*self.size
    return ''.join([row[sub_row:sub_row+self.size] for row in
           self.matrix[sub_col:sub_col+3]])


def check_matrix(self):
    row_repeats = []
    col_repeats = []
    block_repeats = []
    row_invalids = []

    for i in range(len(self.matrix)):
        row_invalids.append(list_invalids(self.matrix[i]))
        row_repeats.append(list_repeats(self.matrix[i]))
        col_repeats.append(list_repeats(column(self, i)))
        block_repeats.append(list_repeats(block(self, i)))

    if len(list(itertools.chain(*row_invalids))) > 0:
        print "invalids: "
        print row_invalids

    if len(list(itertools.chain(*row_repeats))) > 0:
        print "row_repeats: "
        print row_repeats

    if len(list(itertools.chain(*col_repeats))) > 0:
        print "col_repeats: "
        print col_repeats

    if len(list(itertools.chain(*block_repeats))) > 0:
        print "block_repeats"
        print block_repeats



