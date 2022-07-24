# You should re-use and modify your old BoggleBoard class to support the new requirements

# Psuedocode
# iterate through 

import random

class BoggleBoard:

      def __init__(self):
            self.board = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']
            self.board_slots = list(range(16))
            self.found = False
            self.dice = [
            "AAEEGN",
            "ELRTTY",
            "AOOTTW",
            "ABBJOO",
            "EHRTVW",
            "CIMOTU",
            "DISTTY",
            "EIOSST",
            "DELRVY",
            "ACHOPS",
            "HIMNQU",
            "EEINSU",
            "EEGHNW",
            "AFFKPS",
            "HLNNRZ",
            "DEILRX"
            ]
      
      def display_board(self):
            return f"""
                  {self.board[0:4]}
                  {self.board[4:8]}
                  {self.board[8:12]}
                  {self.board[12:16]}
                  """

      def shake(self):
            random.shuffle(self.board_slots)
            for i in range(len(self.board_slots)):
                  letter = self.dice[self.board_slots[i]][self.roll_dice()]
                  if letter == "Q":
                        letter = "Qu"
                  self.board[i] = letter
            return self.display_board()

      def roll_dice(self):
            idx = random.randint(0, 5)
            return idx



      def check_if_word(self, word):
            """
            sets the forward and backwards version of word then checks both directions of diagonal.
            then it calls the recursive helper function include_word to check all of the horizontal and vertical possibilities 
            """
            word = word.upper()
            word_backwards = word[::-1]
            # diagonal
            diagonal_L_to_R = ''.join(self.board[0:16:5])
            if diagonal_L_to_R == word or diagonal_L_to_R == word_backwards:
                        self.found = True
                        return f'found this word diagonally left to right - {word}'
            diagonal_R_to_L = ''.join(self.board[3:15:3])
            if diagonal_R_to_L == word or diagonal_R_to_L == word_backwards:
                        self.found = True
                        return f'found this word diagonally right to left - {word}'

            def include_word(h=0, v=0): 
                  horizontal = ''.join(self.board[h:h+3])
                  vertical = ''.join(self.board[v::4])
                  if word == horizontal or word_backwards == horizontal:
                        self.found = True
                        return f'found this word horizontally - {word}' 
                  elif word == vertical or word_backwards == vertical:
                        self.found = True
                        return f'found this word vertically - {word}' 
                  elif h == 12:
                        return f'{word} not found'
                  else:
                        return include_word(h+4, v+1 )

            return include_word()

            





board1 = BoggleBoard()

quit = False
while quit == False:
      user_input = input(f"press 1 to run the game, 2 to print once, Q to quit - ")
      if user_input == "1":
            count = 0
            board1.found = False
            while board1.found == False:
                  print(board1.shake())
                  print(board1.check_if_word('word'))
                  print(board1.check_if_word('sfse'))
                  print(board1.check_if_word('fdse'))
                  print(board1.check_if_word('chop'))
                  print(board1.check_if_word('free'))
                  print(board1.check_if_word('whgj'))
                  print(board1.check_if_word('erte'))
                  print(board1.check_if_word('oter'))
                  print(board1.check_if_word('maps'))
                  print(board1.check_if_word('taco'))
                  print(board1.check_if_word('leif'))
                  print(board1.check_if_word('hats'))
                  print(board1.check_if_word('leif'))
                  count += 1
                  print(f'count: {count}')
      elif user_input == "Q":
            quit = True
      elif user_input == "2":
            board1.shake()
            print(board1.display_board())
            print(board1.check_if_word('leif'))

