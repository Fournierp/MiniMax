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

    def agent_next_winning_move(self):
        # Agent that plays the next move that wins the board
        board_copy = self.game_board.copy()
        moves = self.get_valid_moves()
        next_move = None
        for move in moves:
            x, y = int(move / 3), int(move % 3)
            board_copy[x][y] = self.player_turn
            for i in range(0, 3):
                # Vertical winner
                if board_copy[0][i] != '-':
                    if self.game_board[0][i] == board_copy[1][i] == board_copy[2][i]:
                        next_move = move
                        break
                # Horizontal winner
                if board_copy[i][0] != '-':
                    if board_copy[i][0] == board_copy[i][1] == board_copy[i][2]:
                        next_move = move
                        break
            # Diagonal winner
            if board_copy[1][1] != '-':
                if board_copy[0][0] == board_copy[1][1] == board_copy[2][2]:
                    next_move = move
                    break
                elif board_copy[2][0] == board_copy[1][1] == board_copy[0][2]:
                    next_move = move
                    break
            # Tie
            for i in range(3):
                for j in range(3):
                    # If there is at least one tile not filed
                    if board_copy[i][j] == '-':
                        next_move = None

            next_move = None
        #
        if next_move is not None:
            return int(next_move / 3), int(next_move % 3)
        else:
            xy = random.choice(moves)
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
                elif self.agent1 == "next_winning":
                    x, y = self.agent_next_winning_move()

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
                elif self.agent2 == "next_winning":
                    x, y = self.agent_next_winning_move()

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
                    elif self.agent1 == "next_winning":
                        x, y = self.agent_next_winning_move()

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
                    elif self.agent2 == "next_winning":
                        x, y = self.agent_next_winning_move()

                    # Put it on the board
                    if self.is_valid_move(x, y):
                        self.game_board[x][y] = 'O'
                        self.player_turn = 'X'
                    else:
                        print('The move is not valid!', x, y)
                        return

        print('Player 1: {} vs. Player 2: {}'.format(self.agent1, self.agent2))
        print('Player 1 W: {}, L: {}, T: {}'.format(w, l, t), end=" ")
