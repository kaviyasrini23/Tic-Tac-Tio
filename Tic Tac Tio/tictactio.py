import os
import time

# Initialize the board with empty spaces
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# List of player symbols. You can add more players here if needed.
players = ['X', 'O', 'A', 'B']  # Player 1 is 'X', Player 2 is 'O', and so on
num_players = len(players)  # Total number of players

# Game status flags
Win = 1      # Flag indicating a win
Draw = -1    # Flag indicating a draw
Running = 0  # Flag indicating the game is still running
Stop = 1     # Flag for stopping the game

Game = Running  # Initialize the game state to 'Running'
current_player = 0  # Index of the current player (Player 1 starts)

# Function to display the board
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("||_")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("||_")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")

# Function to check if the chosen position is valid (i.e., not already taken)
def CheckPosition(x):
    if board[x] == ' ':
        return True  # Position is available
    else:
        return False  # Position is already occupied

# Function to check if there's a winner or if the game is a draw
def CheckWin():
    global Game

    # Check rows for a win
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
    # Check columns for a win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
    # Check diagonals for a win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
    # Check if the board is full (draw)
    elif all(board[i] != ' ' for i in range(1, 10)):
        Game = Draw
    else:
        Game = Running  # The game is still running

# Game Introduction
print("Tic-Tac-Toe Game with Multiple Players!")
print(f"Players: {', '.join(players)}")  # Display player symbols
print("\nPlease wait...")
time.sleep(2)

# Game loop: runs while the game is still in progress
while Game == Running:
    # Clear the screen (cls for Windows, clear for Unix)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Draw the current state of the board
    DrawBoard()

    # Display which player's turn it is
    print(f"Player {current_player + 1}'s turn ({players[current_player]})")
    
    # Ask the current player to choose a position
    choice = int(input("Enter the position between [1-9] where you want to mark: "))
    
    # Check if the chosen position is valid
    if CheckPosition(choice):
        # Mark the board with the current player's symbol
        board[choice] = players[current_player]
        # Move to the next player (wrap around using modulo)
        current_player = (current_player + 1) % num_players
        # Check if there's a winner or if it's a draw
        CheckWin()

    # Clear the screen and display the updated board
    os.system('cls' if os.name == 'nt' else 'clear')
    DrawBoard()

    # If the game ended in a draw, announce it
    if Game == Draw:
        print("It's a Draw!")
    # If someone won, announce the winner
    elif Game == Win:
        # Since current_player was incremented, we subtract 1 to get the last player
        winning_player = (current_player - 1) % num_players
        print(f"Player {winning_player + 1} ({players[winning_player]}) wins!")