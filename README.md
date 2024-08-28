# guess-the-animal-game-using-python-tkinter
# Animal Guessing Game

## Overview

The Animal Guessing Game is a simple and engaging desktop application built with Python's `tkinter` library. In this game, players are given hints about various animals and must guess the animal based on the hint provided. The game features a user-friendly interface where players can enter their name, start the game, and make guesses.

## Features

- **Hint Display**: Provides a hint about an animal.
- **Guess Input**: Allows players to submit their guesses.
- **Attempt Tracking**: Players have a limited number of attempts to guess the animal correctly.
- **Game Reset**: Automatically restarts the game after a win or loss.
## Code Overview
- **AnimalGuessGame Class**: The main class for the game, inheriting from tk.Tk.
- **__init__(self)**: Initializes the main window and sets up the user interface elements.
- **setup_ui(self)**: Configures the layout and widgets for the game.
- **start_game(self)**: Starts a new game, providing a hint and resetting the attempt count.
- **submit_guess(self)**: Handles the player's guess, checks correctness, and updates the attempt count.
- **reset_game(self)**: Resets the game for a new round after a win or loss.
## Usage
- **Enter Your Name**: Type your name into the provided entry field.
- **Start the Game**: Click the "Start Game" button to receive a hint.
- **Submit Your Guess** Enter your guess into the input field and click "Submit Guess."
- **Review Feedback**: You will be notified whether your guess is correct or incorrect, and the number of attempts remaining will be displayed.
- **Restart the Game**: The game will automatically reset after a win or loss, allowing you to play again.
