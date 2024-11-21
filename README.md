# Snake Game

This repository contains a classic Snake Game built in Python using OpenCV for visuals and Pygame for sound effects. The game is simple yet engaging, offering dynamic gameplay with increasing difficulty as the snake grows.  

## Features
- **Smooth Gameplay:** Real-time movement of the snake.
- **Score Tracking:** Earn points by eating apples, with increasing speed for every 5 points scored.
- **Dynamic Challenges:** Avoid collisions with walls and the snake's own body.
- **Interactive Sound Effects:** A satisfying sound plays when the snake eats an apple.

## How to Play
1. Launch the game by running `snake.py`.
2. Use the following keys to control the snake:
   - `I`: Move Up  
   - `J`: Move Left  
   - `K`: Move Down  
   - `L`: Move Right  
   - `P`: Pause the Game  
   - `ESC`: Quit the Game  
3. Avoid collisions and aim to score as high as possible by eating apples.

## Requirements
- Python 3.6 or higher
- OpenCV (`pip install opencv-python`)
- Numpy (`pip install numpy`)
- Pygame (`pip install pygame`)

## File Structure
- **`snake.py`**: The main game logic and code.  
- **Sound Effects**: Ensure `eat_sound.wav` is in the specified path for sound to work properly.

## How It Works
- The snake starts at the center of the board and moves based on player input.  
- Each apple eaten increases the score and the snake’s length.  
- Game over occurs when the snake collides with the wall or itself.  

## Future Enhancements (Planned)
- Add a "Restart Game" option after game over.
- Display the current score during gameplay.
- Allow players to select difficulty levels before starting.

## Credits
This game was developed as a fun project to learn game mechanics using Python, OpenCV, and Pygame.  
