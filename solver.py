from brute_force import BruteForceSolver
from simple_elimination import simple_elimination
from hidden_single import hidden_single
# from coloring import coloring
class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.brute_force_solver = BruteForceSolver(self.puzzle)


    def solve(self):
        # Apply simple elimination and hidden singles techniques
        simple_elimination(self)
        hidden = hidden_single(self)

        # Check if puzzle is solved
        if all(all(cell != 0 for cell in row) for row in self.puzzle):
            return self.puzzle

        # If puzzle is not solved, check if brute force is required
        if not self.find_valid_number():
            raise ValueError("Puzzle is unsolvable.")

        return self.puzzle

    def find_valid_number(self):
        brute_force_solver = BruteForceSolver(self.puzzle)
        if brute_force_solver.solve():
            return True
        return False

        