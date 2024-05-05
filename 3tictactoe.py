import random

class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = ['-'] * 3
            self.board.append(row)

    def get_random_first_player(self):
        return random.choice(['X', 'O'])

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        n = len(self.board)

        for i in range(n):
            if all(self.board[i][j] == player for j in range(n)):
                return True

        for i in range(n):
            if all(self.board[j][i] == player for j in range(n)):
                return True

        if all(self.board[i][i] == player for i in range(n)) or all(self.board[i][n - 1 - i] == player for i in range(n)):
            return True

        return False

    def is_board_filled(self):
        return all(item != '-' for row in self.board for item in row)

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()
        player = self.get_random_first_player()

        while True:
            print(f"Player {player}'s turn")
            self.show_board()

            row, col = map(int, input("Enter row and column numbers to fix spot: ").split())

            self.fix_spot(row - 1, col - 1, player)
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            if self.is_board_filled():
                print("Match Draw!")
                break

            player = self.swap_player_turn(player)

        print()
        self.show_board()

tic_tac_toe = TicTacToe()
tic_tac_toe.start()
