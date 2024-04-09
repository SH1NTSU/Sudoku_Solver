class Sudoku:
    def __init__(self, board) -> None:
       self.board = board
    
    def extract_zones(self,board):
        """Funkcja służąca do przeczytania i wyjęcia 
        liczb z każdej linijki, kolumny, i kwadratu 3x3 (zone)
        nr_elements to znaczy elementy zapełnione nie zera
        """
        zones = []
        # linijki
        for row in  range(0, len(board)):
            zone = {}
            zone["type"] = "row"
            zone["len"] = len(board[row]) - board[row].count(0)
            zone["position"] = row
            self.insert_sorted(zone, zones)
        # kolumny
        for col in range(0,9):
            nr_elements = 0
            for row in range(0,9):
                if board[row][col] != 0:
                    nr_elements += 1
            zone = {}
            zone["type"] = "col"
            zone["len"] = nr_elements
            zone["position"] = col
            self.insert_sorted(zone, zones)
        # kwadraty
        for square in self.generate_square_positions():
            nr_elements
            for row in range(square["row_start"], square["row_end"]+1):
                for col in range(square["col_start"], square["col_end"]+1):
                    if board[row][col] != 0:
                        nr_elements += 1
            zone = {}
            zone["type"] = "square"
            zone["len"] = nr_elements
            zone["position"] = tuple(square.values)
            self.insert_sorted(zone, zones)

        return zones
    
    def generate_square_positions(self):
        """Ta funkcja służy budowie krotki słowników z pozycjami kwadratów"""
        square_positions = []
        row_start = 0
        row_end = 2
        col_start = 0
        col_end = 2

        while len(square_positions) < 9:
            square_positions.append({
                "row_start" : row_start,
                "row_end" : row_end,
                "col_start" : col_start,
                "col_end" : col_end
            })
            if col_start < 6 and col_end < 8:
                col_start += 3
                col_end += 3
            else:
                col_start = 0
                col_end = 2
                row_start += 3
                row_end += 3
    def insert_sorted(zone, zones):
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
                if zone["len"] > zones [i]["len"]:
                    zones.insert(i, zone)
                    inserted = True
                    break
                else:
                    continue
            if not inserted:
                zones.append(zone)
    def insert_possibilities(self,puzzle, row, col):
        """ta funkcja po kolej eliminuje możliwość 
        i jak zostanie już tylko jedno to je dodaje  """
        if puzzle[row][col] == 0:
            row_elements = self.get_zone_elements("row", row, col, puzzle)
            col_elements = self.get_zone_elements("col", row, col, puzzle)
            square_elements = self.get_zone_elements("square", row, col, puzzle)
            numbers = [number for number in range(1, 10)]
            possibilities = [i for i in range(1, 10)]
            for  possibility in numbers:
                if (possibilities in row_elements) or (possibility in col_elements) or (possibility in square_elements):
                    possibilities.remove(possibility)
            if len(possibilities) == 1:
                puzzle[row][col] = possibilities[0]

                
                
    
    def solve(self):
        pass
        
    def print_board(self):
        print("-\t" * 13)
        for row in range(0, len(self.board)):
            formatted_str = "|" + "\t"
            for col in range(0, len(self.board[row])):
                if col in [3, 6]:
                    formatted_str += "|\t"
                formatted_str += str(self.board[row][col]) + "\t"
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
    s = Sudoku(puzzle)
    print('=' * 50)
    s.print_board()
    print('=' * 50)
