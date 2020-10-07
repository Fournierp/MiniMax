import numpy as np
import random


class TicTacToe:
    def __init__(self, player1="random", player2="random", draw=True):
        # Initialise the game board
        self.game_board = self.create_board()
        # Player 1's color
        self.player_turn = 'X'
        # Define how each player will play
        self.agent1 = player1
        self.agent2 = player2

    def create_board(self):
        # Initialise the game board
        return np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])

    def draw_board(self):
        # Print the current board to the screen
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.game_board[i][j]), end=" ")
            print()
        print()

    def is_valid_move(self, x, y):
        # Check that (x, y) is in the board
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        # Check that (x, y) is not filled
        elif self.game_board[x][y] == '-':
            return True

    def get_valid_moves(self):
        # Get the set of empty tiles
        moves = np.empty(0)
        for i in range(3):
            for j in range(3):
                if self.is_valid_move(i, j):
                    moves = np.append(moves, i * 3 + j)
        return moves

    def winner(self):
        # Check all row and columns for winning state
        for i in range(0, 3):
            # Vertical winner
            if self.game_board[0][i] != '-':
                if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i]:
                    return self.game_board[0][i]
            # Horizontal winner
            if self.game_board[i][0] != '-':
                if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2]:
                    return self.game_board[i][0]

        # Diagonal winner
        if self.game_board[1][1] != '-':
            if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2]:
                return self.game_board[1][1]
            elif self.game_board[2][0] == self.game_board[1][1] == self.game_board[0][2]:
                return self.game_board[1][1]

        # Tie
        for i in range(3):
            for j in range(3):
                # If there is at least one tile not filed
                if self.game_board[i][j] == '-':
                    return None

        return '-'

    def agent_random(self):
        # Get a random move from the set of valid ones
        xy = random.choice(self.get_valid_moves())
        return int(xy / 3), int(xy % 3)

    def play(self):

        while True:
            self.draw_board()
            self.result = self.winner()
            # Check if there is an end state
            if self.result != None:
                if self.result == 'X':
                    print('Player 1 won!')
                elif self.result == 'O':
                    print('Player 2 won!')
                elif self.result == '-':
                    print("Tied Game!")
                return None

            # If it's Player 1's turn
            if self.player_turn == 'X':
                # Get Player 1's decison
                if self.agent1 == "random":
                    x, y = self.agent_random()

                # Put it on the board
                if self.is_valid_move(x, y):
                    self.game_board[x][y] = 'X'
                    self.player_turn = 'O'
                else:
                    print('The move is not valid!', x, y)
                    return

            # Player 2's turn
            else:
                # Get Player 2's decison
                if self.agent2 == "random":
                    x, y = self.agent_random()

                # Put it on the board
                if self.is_valid_move(x, y):
                    self.game_board[x][y] = 'O'
                    self.player_turn = 'X'
                else:
                    print('The move is not valid!', x, y)
                    return

    def percentage(self, steps=100, w=0, l=0, t=0):
        #
        for i in range(steps):
            # Empty the board
            self.game_board = self.create_board()

            while True:
                self.result = self.winner()
                # Record the score
                if self.result != None:
                    if self.result == 'X':
                        w += 1
                    elif self.result == 'O':
                        l += 1
                    elif self.result == '-':
                        t += 1
                    break

                # If it's Player 1's turn
                if self.player_turn == 'X':
                    # Get Player 1's decison
                    if self.agent1 == "random":
                        x, y = self.agent_random()

                    # Put it on the board
                    if self.is_valid_move(x, y):
                        self.game_board[x][y] = 'X'
                        self.player_turn = 'O'
                    else:
                        print('The move is not valid!', x, y)
                        return

                # Player 2's turn
                else:
                    # Get Player 2's decison
                    if self.agent2 == "random":
                        x, y = self.agent_random()

                    # Put it on the board
                    if self.is_valid_move(x, y):
                        self.game_board[x][y] = 'O'
                        self.player_turn = 'X'
                    else:
                        print('The move is not valid!', x, y)
                        return

        print('Player 1 W: {}, L: {}, T: {}'.format(w, l, t), end=" ")
