# Pong Game (Pygame)

A simple 2D Pong game built using **Python** and **Pygame**.  
This project is developed step by step to learn the core concepts of game development such as the game loop, object movement, and collision handling.

The game currently includes **two players** and a **moving ball** that rebounds from the screen edges.  
Player–ball collision logic will be implemented next.

---

## Current Features

- Two player paddles
  - Player 1 on the **left side** of the screen
  - Player 2 on the **right side** of the screen
- A ball that moves continuously
- Ball rebounds when it hits:
  - Top edge
  - Bottom edge
  - Left edge
  - Right edge
- Smooth game loop using Pygame
- Game runs at 60 FPS
- Collision detection between ball and players

---

## Features In Progress

- Scoring system
- Game reset and restart logic
- Sound effects

---

## Learning Objectives

- This project is created to practice:
- Game loop implementation
- Object-Oriented Programming (OOP)
- Handling movement and screen boundaries
- Understanding collision detection (upcoming feature)

---

## Future Improvements
- Score display using fonts
- Difficulty levels
- Pause and restart menu

---

## Technologies Used

- Python 3.13
- Pygame

---

## Project Structure

- Pong/
- │
- ├── pong.py # Main game file and game loop
- ├── player.py # Player (paddle) logic
- ├── ball.py # Ball movement and rebound logic
- ├── settings.py # Game settings like ball speed, colors etc.
- ├── README.md


---

## How to Run the Game

1. Install Python (if not already installed)
2. Install Pygame:
   ```bash
   pip install pygame
3. Open terminal and run
  ```bash
   python pong.py


