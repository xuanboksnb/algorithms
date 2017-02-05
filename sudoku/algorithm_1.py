class Sudoku(object):
    def __init__(self, table):
        self.data = [item for row in table for item in row]
        rows = list()
        columns = list()
        zones = list()
        self.empty_its = list()
        # self.cell_to_row = dict()
        # self.cell_to_column = dict()
        # self.cell_to_zone = dict()
        self.solved = False
        self.relates = dict()
        for i in range(9):
            rows.append(list())
            columns.append(list())
        for i in range(3):
            s = list()
            for j in range(3):
                s.append(list())
            zones.append(s)
        for i in range(9):
            for j in range(9):
                it = 9 * i + j
                rows[i].append(it)
                columns[j].append(it)
                zones[i / 3][j / 3].append(it)
                if table[i][j] == 0:
                    self.empty_its.append(it)
                    self.relates[it] = set()
        for i in range(9):
            for it1 in rows[i]:
                if it1 not in self.relates:
                    continue
                for it2 in rows[i]:
                    if it2 != it1:
                        self.relates[it1].add(it2)
        for i in range(9):
            for it1 in columns[i]:
                if it1 in self.relates:
                    for it2 in columns[i]:
                        if it2 != it1:
                            self.relates[it1].add(it2)
        for i in range(3):
            for j in range(3):
                for it1 in zones[i][j]:
                    if it1 in self.relates:
                        for it2 in zones[i][j]:
                            if it2 != it1:
                                self.relates[it1].add(it2)
        # print self.relates

    def _resolve(self, i):
        if i >= len(self.empty_its):
            self.solved = True
            return
        it = self.empty_its[i]  # Cell
        _s = set(self.data[x] for x in self.relates[it] if self.data[x] > 0)
        # s = set(self.cell_to_row[cell_id].values.extend(
        #     self.cell_to_column[cell_id].values.extend(self.cell_to_zone[cell_id].values)))
        candidates = set(i for i in range(1, 10) if i not in _s)
        for _it in candidates:
            self.data[it] = _it
            self._resolve(i + 1)
            if self.solved:
                return
        self.data[it] = 0
        pass

    def resolve(self):
        return self._resolve(0)

    def print_result(self):
        # it1 = 0
        # it2 = 0
        s = ""
        for i in range(9):
            if i % 3 == 0:
                s += "\n"
            for j in range(9):
                if j % 3 == 0:
                    s += " "
                s += " %s" %(self.data[i*9 + j])
            s += "\n"
        print s
        return s


if __name__ == '__main__':
    arr = [[0, 7, 0,  8, 0, 0,  0, 3, 9],
           [0, 0, 1,  0, 0, 0,  0, 0, 2],
           [8, 0, 0,  4, 0, 3,  0, 0, 0],

           [1, 6, 5,  0, 8, 0,  0, 0, 0],
           [0, 0, 0,  2, 0, 4,  0, 0, 0],
           [0, 0, 0,  0, 6, 0,  7, 5, 8],

           [0, 0, 0,  1, 0, 2,  0, 0, 5],
           [4, 0, 0,  0, 0, 0,  9, 0, 0],
           [3, 5, 0,  0, 0, 8,  0, 7, 0]]
    su = Sudoku(arr)
    su.resolve()
    su.print_result()
    # print su.data
