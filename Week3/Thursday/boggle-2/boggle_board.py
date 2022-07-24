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

      def include_word(self):
            pass


      def check_if_word(self, word):
            word = word.upper()
            word_backwards = word[::-1]

            # horizontal
            for i in range(0,16,4):

                  horizontal = ''.join(self.board[i:i+4])
                  if horizontal == word or horizontal == word_backwards:
                        self.found = True
                        return f'found this word - {word}'
            # vert
            for i in range(4):

                  vertical = ''.join(self.board[i::4])
                  if vertical == word or vertical == word_backwards:
                        self.found = True
                        return f'found this word - {word}'

            # diagonal
            diagonal_L_to_R = ''.join(self.board[0:16:5])
            
            if diagonal_L_to_R == word or diagonal_L_to_R == word_backwards:
                        self.found = True
                        return f'found this word - {word}'

            diagonal_list = self.board[3:16:3]
            diagonal_list.pop(len(diagonal_list) -1)
            diagonal_R_to_L = ''.join(diagonal_list)

            if diagonal_R_to_L == word or diagonal_R_to_L == word_backwards:
                        self.found = True
                        return f'found this word - {word}'
            
            return f'{word} not found'





# board1 = BoggleBoard()
# # print(board1.display_board())
# count = 0
# while board1.found == False:
#       print(board1.shake())
#       print(board1.check_if_word('word'))
#       print(board1.check_if_word('sfse'))
#       print(board1.check_if_word('fdse'))
#       print(board1.check_if_word('chop'))
#       print(board1.check_if_word('free'))
#       print(board1.check_if_word('whgj'))
#       print(board1.check_if_word('erte'))
#       print(board1.check_if_word('oter'))
#       print(board1.check_if_word('maps'))
#       print(board1.check_if_word('taco'))
#       print(board1.check_if_word('leif'))
#       print(board1.check_if_word('hats'))
#       print(board1.check_if_word('leif'))
#       count += 1
#       print(f'count: {count}')
