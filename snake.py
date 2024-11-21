import cv2
import numpy as np
from random import choice
import pygame

# Initialize Pygame for sound
pygame.mixer.init()
eat_sound = pygame.mixer.Sound(r"C:\Users\user\OneDrive\Documents\c tutorial\eat_sound.wav")
#game_over_sound = pygame.mixer.Sound("path_to_game_over_sound.wav")  # Add path to the game over sound if you have it

class SnakePart:
    def __init__(self, front, x, y):
        self.front = front
        self.x = x
        self.y = y

    def move(self):
        self.x = self.front.x
        self.y = self.front.y

class Head:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y

    def move(self):
        if self.direction == 0:
            self.x += 1
        elif self.direction == 1:
            self.y += 1
        elif self.direction == 2:
            self.x -= 1
        elif self.direction == 3:
            self.y -= 1

class SnakeGame:
    def __init__(self):
        self.CELL_SIZE = 20
        self.BOARD_SIZE = 45
        self.SPEED = 10  # Adjust the initial speed if necessary

        self.GROWTH = 3
        self.score = 0
        self.quit = False
        self.eaten = True
        self.paused = False
        self.grow = 0
        self.snake = []

        self.head = Head(0, int((self.BOARD_SIZE - 1)/2), int((self.BOARD_SIZE - 1)/2))
        self.snake.append(self.head)

        self.generate_apple()
        print('Controls: I = up, J = left, K = down, L = right, P = pause, ESC = exit')
        self.win_focus()

    def generate_apple(self):
        # Generate a new apple in a location not occupied by the snake
        available_positions = [(x, y) for x in range(self.BOARD_SIZE) for y in range(self.BOARD_SIZE)]
        occupied_positions = [(part.x, part.y) for part in self.snake]
        
        # Remove occupied positions from available positions
        for pos in occupied_positions:
            if pos in available_positions:
                available_positions.remove(pos)
        
        # Randomly choose an available position for the apple
        if available_positions:
            self.applex, self.appley = choice(available_positions)

    def display(self):
        board = np.zeros([self.BOARD_SIZE, self.BOARD_SIZE, 3])
        for part in self.snake:
            board[part.y, part.x] = [0, 255, 0]

        # Draw the apple in red
        board[self.appley, self.applex] = [0, 0, 255]

        cv2.imshow("Snake Game", np.uint8(board.repeat(self.CELL_SIZE, 0).repeat(self.CELL_SIZE, 1)))
        key = cv2.waitKey(int(1000 / self.SPEED))
        
        return key

    def win_focus(self):
        cv2.namedWindow("Snake Game", cv2.WINDOW_AUTOSIZE)
        board = np.zeros([self.BOARD_SIZE * self.CELL_SIZE, self.BOARD_SIZE * self.CELL_SIZE, 3])
        cv2.imshow("Snake Game", board)
        cv2.setWindowProperty("Snake Game", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.waitKey(2000)
        cv2.setWindowProperty("Snake Game", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_AUTOSIZE)

    def run(self):
        while True:
            if self.eaten:
                self.generate_apple()
                self.eaten = False

            key = self.display()

            if key == 8 or key == 27:  # Delete or Escape key
                break
            elif key == ord("l"):  # Move right
                self.head.direction = 0
            elif key == ord("k"):  # Move down
                self.head.direction = 1
            elif key == ord("j"):  # Move left
                self.head.direction = 2
            elif key == ord("i"):  # Move up
                self.head.direction = 3
            elif key == ord("p"):  # Pause key
                self.paused = not self.paused

            if self.paused:
                continue  # Skip the rest of the loop if paused

            for part in self.snake[::-1]:
                part.move()

            if self.head.x < 0 or self.head.x > self.BOARD_SIZE - 1 or self.head.y < 0 or self.head.y > self.BOARD_SIZE - 1:
                self.quit = True
            for part in self.snake[1:]:
                if self.head.x == part.x and self.head.y == part.y:
                    self.quit = True
                    break
            
            if self.quit:
                break

            if self.applex == self.head.x and self.appley == self.head.y:
                subx = self.snake[-1].x
                suby = self.snake[-1].y
                self.eaten = True
                self.grow += self.GROWTH
                self.score += 1
                eat_sound.play()

                if self.score % 5 == 0:
                    self.SPEED += 1
            
            if self.grow > 0:
                self.snake.append(SnakePart(self.snake[-1], subx, suby))
                self.grow -= 1

        self.game_over()

    def game_over(self):
        board = np.zeros([self.BOARD_SIZE * self.CELL_SIZE, self.BOARD_SIZE * self.CELL_SIZE, 3])
        cv2.putText(board, 'Game Over!', (int(self.BOARD_SIZE * self.CELL_SIZE / 4), int(self.BOARD_SIZE * self.CELL_SIZE / 2)),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        cv2.putText(board, f'Final Score: {self.score}', (int(self.BOARD_SIZE * self.CELL_SIZE / 4), int(self.BOARD_SIZE * self.CELL_SIZE / 2) + 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Snake Game", np.uint8(board))
        #game_over_sound.play()  # Play game over sound if you have one
        cv2.waitKey(3000)

if __name__ == '__main__':
    game = SnakeGame()
    game.run()
