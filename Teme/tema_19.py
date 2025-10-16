print("Task 1")
# Write a recursive function for finding the greatest common divisor of two integers.


def great_comm_divizor(a, b):
    if b == 0:
        return a
    return great_comm_divizor(b, a % b)


print(great_comm_divizor(16, 34))

print("Task 2")
# Develop a game of Bulls and Cows. The program chooses a four-digit number, and the player has to guess it.
#  After the user enters a number, the program reports how many digits of the number are guessed (bulls),
#  and how many digits are guessed and stand in the right place (cows). After guessing the number,
#  print the number of user's attempts. Use recursion in your game.

import random

secret_num = str(random.randint(1, 9999))
print("Secret number :", secret_num)


def bulls_cows(secret, attemps=0):
    guess = input("Guess 4-digit number: ")
    attemps += 1

    if len(guess) != 4 or not guess.isdigit():
        print("Invalid input! Enter a 4-digit number.")
        return bulls_cows(secret, attemps)

    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls

    print(f"{bulls} bulls, {cows} cows")
    if guess == secret:
        print(f"Congratulations! You guessed the number in {attemps} attempts.")
        return
    else:
        return bulls_cows(secret, attemps)


bulls_cows(secret_num)


print("Task 3")
# There are an 8×8 chessboard and a knight.
#  The program should request the coordinates of the square from the user and put the knight there.
#  The program's objective is to find the knight's path that allows it to go through the entire chessboard while stepping on each square only once
#  (Since the process of finding a path for initial squares can take a long time,
#  we recommend you to begin with a 6×6 chessboard). Use recursion in your game.


def knight_tour(board, x, y, move):
    if move == len(board) ** 2:
        for row in board:
            print(" ".join(f"{c:2}" for c in row))
        print()
        return True

    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == -1:
            board[nx][ny] = move
            if knight_tour(board, nx, ny, move + 1):
                return True
            board[nx][ny] = -1
    return False


size = 6
board = [[-1] * size for _ in range(size)]
x, y = map(int, input("Start x y (0-5): ").split())
board[x][y] = 0
if not knight_tour(board, x, y, 1):
    print("No solution")

print("Task 4")
# Develop a game of 15 Puzzle.

import random


def print_board(board):
    for row in board:
        print(" ".join(str(x).rjust(2) if x != 0 else "  " for x in row))
    print()


def find_zero(board):
    for i, row in enumerate(board):
        if 0 in row:
            return i, row.index(0)


def move(board, direction):
    x, y = find_zero(board)
    moves = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
    dx, dy = moves.get(direction, (0, 0))
    nx, ny = x + dx, y + dy
    if 0 <= nx < 4 and 0 <= ny < 4:
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
    return board


def is_solved(board):
    return board == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


def play_15_puzzle(board):
    print_board(board)
    if is_solved(board):
        print("🎉 You solved the puzzle!")
        return

    move_dir = input("Move (w/a/s/d): ").lower()
    board = move(board, move_dir)
    play_15_puzzle(board)


nums = list(range(16))
random.shuffle(nums)
board = [nums[i * 4 : (i + 1) * 4] for i in range(4)]

play_15_puzzle(board)
