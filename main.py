class Sudoku:
    def __init__(self, puzzle) -> None:
       self.puzzle = puzzle
    
    def extract_zones(self):
        """Funkcja służąca do przeczytania i wyjęcia 
    liczb z każdej linijki, kolumny, i kwadratu 3x3 (zone)
    nr_elements to znaczy elementy zapełnione nie zera
    """
        zones = []
        # linie
        for row in range(0, len(self.puzzle)):
            zone = {}
            zone["type"] = "row"
            zone["len"] = len(self.puzzle[row]) - self.puzzle[row].count(0)
            zone["position"] = row
            self.insert_sorted(zone, zones)
        # kolumny
        for col in range(0, 9):
            nr_elements = 0
            for row in range(0, 9):
                if self.puzzle[row][col] != 0:
                    nr_elements += 1
            zone = {}
            zone["type"] = "col"
            zone["len"] = nr_elements
            zone["position"] = col
            self.insert_sorted(zone, zones)
        # kwadraty
        for square in self.generate_square_position():
            nr_elements = 0
            for row in range(square["row_start"], square["row_end"] + 1):
                for col in range(square["col_start"], square["col_end"] + 1):
                    if self.puzzle[row][col] != 0:
                        nr_elements += 1
            zone = {}
            zone["type"] = "square"
            zone["len"] = nr_elements
            zone["position"] = tuple(square.values())
            self.insert_sorted(zone, zones)
        return zones
    
    def generate_square_position(self):
        """Ta funkcja służy budowie krotki słowników z pozycjami kwadratów"""
        square_positions = []
        row_start = 0
        row_end = 2
        col_start = 0
        col_end = 2

        while len(square_positions) < 9:
            square_positions.append({
                "row_start": row_start,
                "row_end": row_end,
                "col_start": col_start,
                "col_end": col_end
            })
            if col_start < 6 and col_end < 8:
                col_start += 3
                col_end += 3
            else:
                col_start = 0
                col_end = 2
                row_start += 3
                row_end += 3
        return square_positions
    
    def insert_sorted(self, zone, zones):
        """Ta funkcja bierze słownik określający 
    daną strefe i wrzuca ją do listy straf po długość pola. 
    Robie to po to żeby było posortowane i 
    żeby zaczynało od tych stref z większą ilośćą pól. 
    To usprawni kod w prędkość rozwiązywania """
        if len(zones) == 0:
            zones.append(zone)
        else:
            inserted = False
            for i in range(0, len(zones)):
                if zone["len"] > zones[i]["len"]:
                    zones.insert(i, zone)
                    inserted = True
                    break
                else:
                    continue
            if not inserted:
                zones.append(zone)
    
    def insert_possibilities(self, row, col):
        """ta funkcja po kolej eliminuje możliwość 
    i jak zostanie już tylko jedno to je dodaje  """
        if self.puzzle[row][col] == 0:
            row_elements = self.get_zone_elements("row", row, col)
            col_elements = self.get_zone_elements("col", row, col)
            square_elements = self.get_zone_elements("square", row, col)
            numbers = [number for number in range(1, 10)]
            possibilities = [i for i in range(1, 10)]
            for possibility in numbers:
                if (possibility in row_elements) or (possibility in col_elements) or (possibility in square_elements):
                    possibilities.remove(possibility)
            if len(possibilities) == 1:
                self.puzzle[row][col] = possibilities[0]
    
    def get_zone_elements(self, zone_type, position1, position2):
        """ta funkcja bierze wrzystkkie nie 
    zerowe elementy z danej strefy(lini, kolumny albo kwadratu)
    """
        elements = []
        if zone_type == "col":
            for row in range(0, 9):
                if self.puzzle[row][position2] != 0:
                    elements.append(self.puzzle[row][position2])
        elif zone_type == "row":
            for col in range(0, 9):
                if self.puzzle[position1][col] != 0:
                    elements.append(self.puzzle[position1][col])
        else:
            square_position = self.generate_square_position()
            for square in square_position:
                if (square["row_start"] <= position1 <= square["row_end"]
                    and square["col_start"] <= position2 <= square["col_end"]):
                    for row in range(square["row_start"], square["row_end"] + 1):
                        for col in range(square["col_start"], square["col_end"] + 1):
                            if self.puzzle[row][col] != 0:
                                elements.append(self.puzzle[row][col])
        return elements

    def solve(self):
        for iterations in range(0, 3):
            zones = self.extract_zones()
            for zone in zones:
                if zone["type"] == "row":
                    row = zone["position"]
                    for col in range(0, 9):
                        self.insert_possibilities(row, col)
                elif zone["type"] == "col":
                    col = zone["position"]
                    for row in range(0, 9):
                        self.insert_possibilities(row, col)
                else:
                    row_start = zone["position"][0]
                    row_end = zone["position"][1]
                    col_start = zone["position"][2]
                    col_end = zone["position"][3]
                    for row in range(row_start, row_end + 1):
                        for col in range(col_start, col_end + 1):
                            self.insert_possibilities(row, col)
        return self.puzzle
    
    def print_board(self):
        """Ta funkcjia tworzy planszę sudoku"""
        print("-\t" * 13)
        for row in range(0, len(self.puzzle)):
            formatted_str = "|" + "\t"
            for col in range(0, len(self.puzzle[row])):
                if col in [3, 6]:
                    formatted_str += "|\t"
                formatted_str += str(self.puzzle[row][col]) + "\t"
            formatted_str += "|"
            print(formatted_str)
            if row in [2, 5]:
                print("-\t" * 13)
        print("-\t" * 13)

if __name__ == "__main__":
    puzzle = [
        [8, 7, 6, 9, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 6, 0, 0, 0],
        [0, 4, 0, 3, 0, 5, 8, 0, 0],
        [4, 0, 0, 0, 0, 0, 2, 1, 0],
        [0, 9, 0, 5, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 4, 0, 3, 0, 6],
        [0, 2, 9, 0, 0, 0, 0, 0, 8],
        [0, 0, 4, 6, 9, 0, 1, 7, 3],
        [0, 0, 0, 0, 0, 1, 0, 0, 4]
    ]
    solver = Sudoku(puzzle)
    print("Original Puzzle:")
    solver.print_board()
    solver.solve()
    print("=" * 31)
    print("Solved Puzzle:")
    solver.print_board()
