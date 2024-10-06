# Tic-Tac-Toe Game with Multiple Players

This is a **Tic-Tac-Toe** game that supports multiple players. The default symbols for the players are `X`, `O`, `A`, and `B`, but you can modify the list to include more players if needed.

## How to Play

- Each player takes turns to mark their symbol on a 3x3 grid.
- A player wins if they are able to place three of their symbols in a horizontal, vertical, or diagonal row.
- If all nine spaces are filled without a winner, the game results in a draw.

## Game Instructions

1. Players are assigned symbols in the following order: `X`, `O`, `A`, `B`.
2. Each player, in their turn, selects a position on the board by entering a number between `1` and `9`. The positions correspond to the layout below:


 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9


3. The game continues until there is a winner or the board is full (resulting in a draw).
4. The game will announce if a player wins or if the game ends in a draw.

## Code Breakdown

- The "board" is a list of characters representing the 3x3 grid. Initially, all positions are empty (`' '`).
- The "players" list contains the symbols for each player. Modify this list if you want to add more players.
- The game is managed by three status flags: "Win", "Draw", and "Running", which represent the possible states of the game.
- The "DrawBoard" function visually displays the board during each player's turn.
- The "CheckPosition" function ensures that a player can't select an already occupied spot.
- The "CheckWin" function checks for a winner or a draw after each move.

## Running the Game

To run the game, follow these steps:

1. "Install Python": Ensure you have Python installed on your system.
2. "Run the script": Open a terminal or command prompt and run the script by typing:

   # bash:
   
   python tic_tac_toe.py
   
4. The game will guide you through the rest!

# Example Gameplay

  Player 1 (X) chooses position 1.
  Player 2 (O) chooses position 5.
  Player 3 (A) chooses position 9.
  Player 4 (B) chooses position 2.

Continue taking turns until there's a winner or a draw.
