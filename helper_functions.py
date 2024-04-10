class SudokuHelper:
    @staticmethod
    def extract_zones(puzzle):
        """Funkcja służąca do przeczytania i wyjęcia 
    liczb z każdej linijki, kolumny, i kwadratu 3x3 (zone)
    nr_elements to znaczy elementy zapełnione nie zera
    """
        zones = []
        # linie
        for row in range(0, len(puzzle)):
            zone = {}
            zone["type"] = "row"
            zone["len"] = len(puzzle[row]) - puzzle[row].count(0)
            zone["position"] = row
            SudokuHelper.insert_sorted(zone, zones)
        # kolumny
        for col in range(0, 9):
            nr_elements = 0
            for row in range(0, 9):
                if puzzle[row][col] != 0:
                    nr_elements += 1
            zone = {}
            zone["type"] = "col"
            zone["len"] = nr_elements
            zone["position"] = col
            SudokuHelper.insert_sorted(zone, zones)
        # kwadraty
        for square in SudokuHelper.generate_square_position():
            nr_elements = 0
            for row in range(square["row_start"], square["row_end"] + 1):
                for col in range(square["col_start"], square["col_end"] + 1):
                    if puzzle[row][col] != 0:
                        nr_elements += 1
            zone = {}
            zone["type"] = "square"
            zone["len"] = nr_elements
            zone["position"] = tuple(square.values())
            SudokuHelper.insert_sorted(zone, zones)
        return zones

    @staticmethod
    def generate_square_position():
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

    @staticmethod
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
                if zone["len"] > zones[i]["len"]:
                    zones.insert(i, zone)
                    inserted = True
                    break
                else:
                    continue
            if not inserted:
                zones.append(zone)

    @staticmethod
    def insert_possibilities(puzzle, row, col):
        """ta funkcja po kolej eliminuje możliwość 
    i jak zostanie już tylko jedno to je dodaje  """
        if puzzle[row][col] == 0:
            row_elements = SudokuHelper.get_zone_elements(puzzle, "row", row, col)
            col_elements = SudokuHelper.get_zone_elements(puzzle, "col", row, col)
            square_elements = SudokuHelper.get_zone_elements(puzzle, "square", row, col)
            numbers = [number for number in range(1, 10)]
            possibilities = [i for i in range(1, 10)]
            for possibility in numbers:
                if (possibility in row_elements) or (possibility in col_elements) or (possibility in square_elements):
                    possibilities.remove(possibility)
            if len(possibilities) == 1:
                puzzle[row][col] = possibilities[0]

    @staticmethod
    def get_zone_elements(puzzle, zone_type, position1, position2):
        """ta funkcja bierze wrzystkkie nie 
    zerowe elementy z danej strefy(lini, kolumny albo kwadratu)
    """
        elements = []
        if zone_type == "col":
            for row in range(0, 9):
                if puzzle[row][position2] != 0:
                    elements.append(puzzle[row][position2])
        elif zone_type == "row":
            for col in range(0, 9):
                if puzzle[position1][col] != 0:
                    elements.append(puzzle[position1][col])
        else:
            square_position = SudokuHelper.generate_square_position()
            for square in square_position:
                if (square["row_start"] <= position1 <= square["row_end"]
                        and square["col_start"] <= position2 <= square["col_end"]):
                    for row in range(square["row_start"], square["row_end"] + 1):
                        for col in range(square["col_start"], square["col_end"] + 1):
                            if puzzle[row][col] != 0:
                                elements.append(puzzle[row][col])
        return elements
