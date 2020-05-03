class Cell:
    def __init__(self, num_of_cells: int):
        self.num_of_cells = num_of_cells

    def __add__(self, other):
        return self.num_of_cells + other.num_of_cells

    def __sub__(self, other):
        if self.num_of_cells - other.num_of_cells > 0:
            return self.num_of_cells - other.num_of_cells
        else:
            return 'The operation cannot be performed'

    def __mul__(self, other):
        return self.num_of_cells * other.num_of_cells

    def __truediv__(self, other):
        return self.num_of_cells // other.num_of_cells

    def make_order(self, row_length):
        num_of_lines = self.num_of_cells // row_length
        new_string = (('*' * row_length) + '\n') * num_of_lines + '*' * (self.num_of_cells % row_length)
        return new_string


cell1 = Cell(21)
cell2 = Cell(8)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(4))
