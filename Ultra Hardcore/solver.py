from brute_force import BruteForceSolver
from simple_elimination import simple_elimination
from hidden_single import hidden_single
class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.brute_force_solver = BruteForceSolver(self.puzzle)

    def solve(self):
        while True:
            hidden_singles = hidden_single(self.puzzle) 
            if hidden_singles > 0:     
                simple_elimination(self.puzzle)


            if self.is_solved():
                break
            
            if hidden_singles == 0 and self.is_unsolved_cells_exist():
                self.brute_force_solver.solve()

        return self.puzzle

    def is_solved(self):
        return all(0 not in row for row in self.puzzle)

    def is_unsolved_cells_exist(self):
        return any(0 in row for row in self.puzzle)