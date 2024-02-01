# Description
This is a simple application that mimicks the game [Simon](https://en.wikipedia.org/wiki/Simon_(game)). I built this to primarily help children and teens learn about the fundamentals of programming.

# Usage
You may use this project however you see fit.

# How to start
Ensure you have [Python](https://www.python.org/downloads/) installed, and optionally use an IDE. Clone the repository and run the game with `python3 main.py`.

# How to play
Use `QWAS` keys, corresponding to 4 corners of a square. Memorize the order that the squares light up and try repeating it.

# How it works
It uses emojis to represent 4 segments of the board. The program will activate the square corresponding to the `QWAS` keys. The game uses a queue to keep track of the order of buttons, and a buffer to convert user input so it would be easier to interpret.
