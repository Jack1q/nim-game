# To - do: add nim sum

class Game:

    def __init__(self):
        self.board = [
            [' ',' ',' ', '!',' ',' ',' '],
            [' ',' ','!','!','!',' ',' '],
            [' ','!','!','!','!','!',' '],
            ['!','!','!','!','!','!','!']
        ]

    def display_board(self):
        for x, row in enumerate(self.board):
            print(f"{x}:", end=' ')
            for col in row:
                print(col, end=' ')
            print()

    def matches_left_on_board(self):
        return any(['!' in row for row in self.board])

    def row_sum(self, row):
        return self.board[row].count('!') if 0 <= row <= 3 else 0

    def make_move(self, row, number_of_matches):
        if number_of_matches > self.row_sum(row):
            return False
        for x in range(number_of_matches):
            self.board[row][self.board[row].index('!')] = ' '
        return self.board

    def play_game(self):
        turn = 0
        while self.matches_left_on_board():
            print(f"Player {'2' if turn % 2 else '1'}'s Turn")
            self.display_board()
            row, number_of_matches = -999,-999
            while self.row_sum(row) == 0:
                row = int(input('Enter row to remove matches from (0-3) > '))
            while not (1 <= number_of_matches <= self.row_sum(row)):
                number_of_matches = int(input(f'Enter number of matches to remove from row {row} ({self.row_sum(row)} left) > '))
            self.make_move(row, number_of_matches)
            turn += 1
        print(f"Player {turn % 2 + 1} wins!")

if __name__ == '__main__':
    game = Game().play_game()
