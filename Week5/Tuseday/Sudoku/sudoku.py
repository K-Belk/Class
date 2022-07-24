

class SudokuSolver:
    def __init__(self, board_string):
        self.board_list = list(map(int, board_string))
        self.domains = [1,2,3,4,5,6,7,8,9]
        self.positions = []

    def solve(self):
        """
        Iterates through and fills the board with one of the available guesses and backtracks when it finds a spot that has no available guesses
        """
        index = 0
        while index != 81:
            row_start = (index // 9)*9
            row_end = row_start + 9
            column = index % 9
            if self.board_list[index] != 0:
                index +=1
            else:
                available = self.check_spot(row_start, row_end, column)
                if available:
                    guess = available.pop(0)
                    self.board_list[index] = guess
                    self.positions.append([index, available])
                    index += 1
                else:
                    index = self.backtrack()
        self.print_board()
        return "      -------SOLVED--------"

    def backtrack(self):
        """
        Backs up until if finds a filed index with other posabilities and picks a new one. Clears board spaces as it backtracks
        """
        if self.positions[-1][1]:
            guess = self.positions[-1][1].pop(0)
            index = self.positions[-1][0]
            self.board_list[index] = guess
            return index
        else:
            clear = self.positions.pop()
            index = clear[0]
            self.board_list[index] = 0
            return self.backtrack()

    def check_row(self, row_start, row_end):
        """
        Checks the row and returns a list of used values
        """
        rows_list = [elm for elm in self.board_list[row_start:row_end] if elm != 0]
        return rows_list

    def check_column(self, column):
        """
        Checks the column and returns a list of used values
        """
        column_list = []
        for row in range(9):
            if self.board_list[column + (row*9) ] != 0:
                column_list.append(self.board_list[column + (row*9)])
        return column_list

    def check_square(self,row_start, column):
        """
        Checks the square and returns a list of used values
        """
        square_list = []
        row_start = (row_start//27)*27
        for idx in range(3):
            square_start = (((column // 3)*3) + row_start)
            square_list.append(self.board_list[square_start:square_start+3])
            row_start += 9
        square_list = [item for sublist in square_list for item in sublist]
        square_list = [elm for elm in square_list if elm != 0]
        return square_list

    def check_spot(self, row_start, row_end, column):
        """
        Check each row, column and square for what is used then returns a list of available choices
        """
        row_list = self.check_row(row_start, row_end)
        column_list = self.check_column(column)
        square_list = self.check_square(row_start, column)
        used = []
        used.append(row_list)
        used.append(column_list)
        used.append(square_list)
        used = list(set([item for sublist in used for item in sublist]))
        avail = [not_used for not_used in self.domains if not_used not in used]
        return avail

    def print_board(self):
        """
        Prints out the game board with foramting
        """
        output = ''
        for idx, string in enumerate(self.board_list):
            string_idx = idx + 1
            if idx % 27 == 0:
                output += '_' * 32 + "\n"
            if string == '0':
                output += "   "
            else:
                output += f" {string} "
            if string_idx % 9 == 3 or string_idx % 9 == 6:
                output += " | "
            if string_idx % 9 == 0:
                output += "\n"
        print(output)


