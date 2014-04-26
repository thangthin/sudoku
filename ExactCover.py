class Node(object):
    def __init__(self, row, header):
        self.data = None
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.row = row
        self.header = header


class Header(object):
    def __init__(self, col, left, right):
        self.col = col
        self.left = left
        self.right = right
        self.up = self
        self.down = self
        self.col_hd = None


class DancingLink():
    def __init__(self):
        self.headers = []
        self.root = Header(0, None, None)
        self.root.left = self.root
        self.root.right = self.root
        self.headers.append(self.root)

    def create_headers(self, col):
        for col in range(col):
            h = Header(col + 1, self.headers[col], self.root)
            self.headers[col].right = h
            self.root.left = h
            self.headers.append(h)
        return self.headers

    def create_row(self, row, cols, headers):
        self.headers = headers
        neighbors = []
        for i in cols:
            node = Node(row, self.headers[i])
            if self.headers[i].down != self.headers[i]:
                node.up = self.headers[i].up
                node.down = self.headers[i]
                self.headers[i].up.down = node
                self.headers[i].up = node
            else:
                self.headers[i].up = node
                self.headers[i].down = node
            if neighbors:
                node.left = neighbors[0].left
                node.right = neighbors[0]
                neighbors[0].left.right = node
                neighbors[0].left = node
            neighbors.append(node)

    def create_matrix(self, col, rows):
        self.headers = self.create_headers(col)
        for i in range(len(rows)):
            DancingLink().create_row(i, rows[i], self.headers)

        self.cover(self.root.left)

        hd = self.root.right

        while hd != self.root:
            node = hd.down
            while node != hd:
                s = node.row, node.header.col
                print s,
                node = node.down
            print ""
            hd = hd.right





        #self.solve()

    def cover(self, header):
        node = header.down
        while node != header:
            node.up.down = node.down
            node.down.up = node.up
        header.left.right = header.right
        header.right.left = header.left








        """
        while node.down != node:
            while node.right != node:
                node.up.down = node.down
                node.down.up = node.up
                """


    def uncover(self, header):
        header.right.left = header
        header.left.right = header

    def cover_row(self, node):
        self.cover(node.header)
        next_node = node.right
        while not(next_node == node):
            self.cover(next_node.header)
            next_node = next_node.right

    def uncover_row(self, node):
        self.uncover(node.left.header)
        prev_node = node.left.left
        while not(prev_node == node.left):
            self.uncover(prev_node.header)
            prev_node = prev_node.left

    def search(self):
        sol = []
        header = self.root.right
        while not(self.root.right == self.root):
            self.cover(header)
            node = header.col_hd.down
            for i in header.col_list:
                sol.append(i)
                self.cover_row(i)





constraint = [[1, 4, 7],
              [1, 4],
              [4, 5, 7],
              [3, 5, 6],
              [2, 3, 6, 7],
              [2, 7]]

DancingLink().create_matrix(7, constraint)





