from sudoku import SudokuSolver
import csv



with open('sample_sudoku_board_inputs.csv') as csv_file:
    game_boards = csv.reader(csv_file)
    for index, board in enumerate(game_boards):
        board = ''.join(board[0])
        print(f"""
    -------------------------
            Game {index + 1}
    -------------------------
        """)
        game = SudokuSolver(board)
        print(game.solve())
