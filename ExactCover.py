class Node():
    def __init__(self, row, col, header):
        self.up, self.down = self, self
        self.left, self.right = self, self
        self.row, self.col = row, col
        self.header = header

    def cover_node(self):
        self.up.down = self.down
        self.down.up = self.up

    def uncover_node(self):
        self.up.down = self
        self.down.up = self

class Header():
    def __init__(self, col):
        self.up, self.down = self, self
        self.left, self.right = self, self
        self.row = -1
        self.col = col

    def cover_header(self):
        self.left.right = self.right
        self.right.left = self.left

    def uncover_header(self):
        self.left.right = self
        self.right.left = self


class Matrix():
    def __init__(self, cons, rows):
        self.rows, self.cons = rows, cons
        self.headers = []
        self.root = Header(-1)
        self.headers.append(self.root)
        self.node_count = 0
        self.create_matrix()

    def create_headers(self):
        for c in range(self.cons):
            h = Header(c)
            h.right = self.root
            h.left = self.headers[c]
            self.headers[c].right = h
            self.root.left = h
            self.headers.append(h)
            self.node_count += 1

    def create_row(self, n, cons):
        links = []
        for i in cons:
            node = Node(n, i, self.headers[i+1])
            node.up = node.header.up
            node.down = node.header
            node.header.up.down = node
            node.header.up = node
            links.append(node)
            node.left = links[0].left
            node.right = links[0]
            links[0].left.right = node
            links[0].left = node
            self.node_count += 1

    def create_matrix(self):
        self.create_headers()
        for i in range(len(self.rows)):
            self.create_row(i, self.rows[i])

        return self.root

    def print_matrix(self):
        hd = self.root.right
        while hd != self.root:
            print hd.col,
            node = hd.down
            while node != hd:
                s = node.row,
                print s,
                node = node.down
            print ""
            hd = hd.right


class DancingLink():
    def __init__(self, n, s):
        self.solution = []
        self.sm = Matrix(n, s)
        self.col = self.sm.root.right

    def cover(self, node):
        n = node
        while True:
            c = n.left.header
            c.cover_header()
            i = c.down
            while i != c:
                j = i.right
                while j != i:
                    j.cover_node()
                    j = j.right
                i = i.down
            n = n.right
            if n == node:
                break

    def uncover(self, node):
        n = node
        while True:
            c = n.header
            i = c.up
            while i != c:
                j = i.left
                while j != i:
                    j.uncover_node()
                    j = j.left
                i = i.up
            c.uncover_header()
            n = n.left
            if n == node:
                break

    def search(self):
        self.col = self.sm.root.right
        col = self.col

        if col == self.sm.root:
            return True
        if col.down == col:
            return False

        row = col.down
        while row != col:
            self.cover(row)
            if self.search():
                self.solution.append(row)
                return True
            self.uncover(row)
            row = row.down

        return False


# subset = [[1, 4, 7],
#           [1, 4],
#           [4, 5, 7],
#           [3, 5, 6],
#           [2, 3, 6, 7],
#           [2, 7]]
#
# DancingLink(7, subset).sm.print_matrix()





