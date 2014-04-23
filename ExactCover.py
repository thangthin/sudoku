class Node(object):
    def __init__(self, row, header, up, down):
        self.number = 0
        self.left = None
        self.right = None
        self.up = up
        self.down = down
        self.row = row
        self.header = header


class Header(object):
    def __init__(self, col, left, right):
        self.col = col
        self.left = left
        self.right = right
        self.col_list = []


class DancingLink():
    def __init__(self, matrix):
        self.headers = []
        self.root = Header(0, None)
        self.root.left = self.root
        self.root.right = self.root

    def new_node(self, row, col):
        if not self.headers[col].col_list:
            self.headers[col].col_list.append(Node(row, self.headers[col]))
            self.headers[col].col_list[0].up = self.headers[col].col_list[0]
            self.headers[col].col_list[0].down = self.headers[col].col_list[0]
        else:
            self.headers[col].col_list.append(Node(row, self.headers[col]))
            self.headers[col].col_list[0].down = self.headers[col].col_list[0]
            self.headers[col].col_list[0].up = self.headers[col].col_list[0]


    def generate_problem(self):
        self.headers.append(self.root)
        for i in range(0, (81 * 4)):
            self.headers.append(
                Header(i, self.headers[i - 1], self.root))
            self.headers[i].left.right = self.headers[i]
            self.headers[0].right = self.headers[i]

        for row in range(1, 10):
            for col in range(1, 10):
                for num in range(1, 10):
                    self.new_node(row)
                    self.headers[((row - 1) * 9) + col].append(
                        Node(row, self.headers[((row - 1) * 9) + col]))


DancingLink(object).generate_problem()







