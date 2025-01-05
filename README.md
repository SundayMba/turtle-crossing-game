This code implements a simple Raccoon Crossing Game using Python's turtle module and pygame for sound effects. Here's a brief overview:

Key Features:
1.⁠ ⁠Game Setup:
•⁠ ⁠A screen of size 800x800 is created with turtle.
•⁠ ⁠A raccoon character (raccoon2.gif) replaces the default turtle shape, and cars (attacker2.gif) serve as obstacles.
2.⁠ ⁠Player Movement:
•⁠ ⁠The Player class manages the raccoon character, allowing it to move in four directions using the arrow keys.
3.⁠ ⁠Managing Crossing Raccoons:
•⁠ ⁠The CarManager class generates and moves the attackers across the screen. An attacker is added at random intervals and move faster as the player progresses through levels.
4.⁠ ⁠Collision Detection:
•⁠ ⁠The game checks for collisions between the raccoon and attacker. If a collision occurs, the game ends with a "Game Over" message.
5.⁠ ⁠Scoring:
•⁠ ⁠The Scoreboard class tracks the player's progress, increasing the level whenever the raccoon crosses the finish line and resetting its position.
6.⁠ ⁠Sound Effects:
•⁠ ⁠A sound (shoot.mp3) is played when triggered, using pygame.mixer.music.play() for enhanced engagement.

### requirements

- install the neccessary requirements by running
  `pip install -r requirements.txt`

- make sure you have python version 3 installed
- start the game by running
  `python3 main.py`
