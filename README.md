# Number Guessing Game

Welcome to the **Number Guessing Game**! 🎉 This game lets you guess a randomly chosen number between 1 and 100. You'll have the option to choose between two difficulty levels: **Easy** or **Hard**. Try to guess the number within the allowed attempts, and see if you can win!

## Table of Contents
- [How to Play](#how-to-play)
- [Features](#features)
- [Getting Started](#getting-started)
- [Code Structure](#code-structure)
- [How to Run the Game](#how-to-run-the-game)
- [Example](#example)
- [Requirements](#requirements)

---

## How to Play

1. When you start the game, you'll be asked to pick a difficulty level:
   - **Easy**: You get 10 attempts to guess the number.
   - **Hard**: You get only 5 attempts.

2. Enter your guess, and the game will tell you if it's **too high** or **too low**.
3. Keep guessing until you find the correct number or run out of attempts.
4. When the game ends, you’ll have the option to play again if you want.

---

## Features

- **Random Number Generation**: The game picks a new number each time you play, so it’s different every round.
- **Difficulty Levels**: Choose between *Easy* and *Hard* modes, with different numbers of attempts.
- **Replay Option**: You can keep playing as many times as you want by choosing to play again at the end.

---

## Getting Started

Before running the game, make sure you have Python installed. You can check if Python is installed by typing `python --version` in your terminal or command prompt.

This game also uses some external images/logos (like `logo`, `you_lose_logo`, and `logo_end`) to make it more fun, which are assumed to be in an `art` module. Make sure you have the `art.py` file if you want the logos to display.

---

## Code Structure

- **`play_easy()`**: This function runs the game in easy mode with 10 guesses.
- **`play_hard()`**: This function runs the game in hard mode with 5 guesses.
- **`play_game(user_difficulty)`**: This function selects which difficulty mode to start based on your choice.
- **`random_number`**: A new random number between 1 and 100 is generated each time the game starts.
- **Main Game Loop**: After each game, you’re asked if you want to play again, and the game restarts if you choose to.

---

## How to Run the Game

1. Save this code in a Python file, for example, `number_guessing_game.py`.
2. In the terminal or command prompt, navigate to the folder where you saved the file.
3. Run the game by typing:
   ```bash
   python number_guessing_game.py
   ```

---

## Example

When you start the game, the following message will appear:
```
Welcome to the Number Guessing Game!!
I'm thinking of a number between 1 and 100.
Choose a Difficulty, 'easy' or 'hard': 
```

- If you choose **easy**, you will have 10 attempts.
- If you choose **hard**, you will have 5 attempts.

Each time you make a guess, you’ll get feedback like "Too Low" or "Too High" until you find the correct answer or run out of guesses.

---

## Requirements

- Python 3.x
- `art.py` module with the required logos (e.g., `logo`, `you_lose_logo`, `logo_end`)
