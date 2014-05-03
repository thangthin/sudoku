
class SatSolver():
    def __init__(self, c):
        self.clauses = c
        self.var_dict = {}
        self.create_var_dict()
        self.solution = []
        self.remove_list = []
        self.solve()

    def create_var_dict(self):
        for c in range(len(self.clauses)):
            for i in self.clauses[c]:
                if self.var_dict.has_key(abs(i)):
                    self.var_dict[abs(i)].append(c)
                else:
                    self.var_dict[abs(i)] = [c]

        return self.var_dict

    def is_unit_clause(self, c):
        return len(c) == 1

    def unit_propagate(self, var):
        for i in self.var_dict[abs(var)]:
            c = self.clauses[i]
            if var in c: self.remove_list.append(i)
            else: c.remove(-var)
        self.solution.append(var)
        del self.var_dict[abs(var)]

    def is_pure(self, var):
        for i in self.var_dict[abs(var)]:
            if not var in self.clauses[i]:
                return False
        return True

    def pure_lit_assign(self, var):
        for i in self.var_dict[abs(var)]:
            for v in self.clauses[i]:
                self.var_dict[abs(v)].remove(i)
            del self.clauses[i]
        self.solution.append(var)
        self.remove_list.append(abs(var))
        print self.solution

    def solve(self):
        if not self.clauses:
            print True
            print self.solution
            return True
        for c in self.clauses:
            if not self.clauses[c]:
                print False
                return False
            else:
                print self.clauses[c],

        for c in self.clauses:
            if self.is_unit_clause(self.clauses[c]):
                self.unit_propagate(self.clauses[c][0])

        for c in self.remove_list:
            for i in self.clauses[c]:
                if self.var_dict.has_key(i):
                    self.var_dict[i].remove(c)
                    if not self.var_dict[i]:
                        del self.var_dict[i]
            del self.clauses[c]
            self.remove_list = []

        for v in self.var_dict:
            if v in self.clauses[self.var_dict[v][0]]: lit = v
            else: lit = -v
            if self.is_pure(lit):
                self.pure_lit_assign(lit)

        for c in self.remove_list:
            del self.var_dict[c]
            self.remove_list = []



        self.solve()


# c = {0:[1,2],
#      1:[-1,3],
#      2:[-3,4],
#      3:[1],
#      4:[-2, -3]}
#
#
# SatSolver(c)




