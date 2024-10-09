# Wordle Game

A simple, console-based Wordle game built in Python. The game challenges users to guess a randomly selected 5-letter word within 5 attempts.

## Features
- **Rounds**: 5 attempts to guess the word.
- **Word Length**: Each word is 5 letters long.
- **Feedback**:
  - Correct letters in the correct position are shown in **UPPERCASE**.
  - Correct letters in the wrong position are shown in **lowercase**.
  - Incorrect letters are displayed in a list of attempted letters.

## How to Play
1. The game selects a random word from the provided `WORDS.csv` file.
2. Players enter their guesses through console prompts.
3. After each guess, the console provides feedback on letter accuracy and placement.

## Prerequisites
- No external libraries are required, except for the standard Python library (`random` is used).
- Ensure the `WORDS.csv` file is in the same directory as the Python script for the game to function.

## Usage
1. Clone the repository to your local machine.
2. Ensure the `WORDS.csv` file is present.
3. Run the Python script in your console:

   ```bash
   python wordle_game.py
   ```

4. Follow the prompts to start playing!

## File Structure
- `wordle_game.py`: Main Python script to run the game.
- `WORDS.csv`: A CSV file containing a list of 5-letter words for the game.

## Logic Overview
- The game randomly picks a word from the `WORDS.csv` file.
- After each guess, feedback is provided based on the accuracy of each letter:
  - Letters in the correct position are capitalized.
  - Letters in the word but in the wrong position are displayed in lowercase.
  - Incorrect letters are added to a list for reference in future guesses.
