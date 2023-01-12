from math import sqrt
import time


class Snake:

    def __init__(self, length):
        self.snake = self.setup_snake(length)

    def move_snake(self, direction, times):
        current_pos, prev_head_pos = [0, 0], [0, 0]
        for i in range(int(times)):
            for k in range(len(self.snake)):
                if k == 0:
                    prev_head_pos = self.snake[0].copy()
                    if direction == 'U':
                        self.snake[0][0] += 1
                    elif direction == 'D':
                        self.snake[0][0] -= 1
                    elif direction == 'L':
                        self.snake[0][1] -= 1
                    elif direction == 'R':
                        self.snake[0][1] += 1

                elif not self.is_in_range(self.snake[k - 1], self.snake[k]):
                    current_pos = self.snake[k]
                    self.snake[k] = prev_head_pos
                    prev_head_pos = current_pos
            self.print_board()
            time.sleep(0.35)

    def print_board(self):
        for i in range(6, -1, -1):
            for k in range(25):
                if [i, k] in self.snake:
                    print('S', end="")
                else:
                    print('x', end="")
            print('')
        print('')

    @staticmethod
    def setup_snake(num):
        snake = []
        for i in range(num):
            snake.append([0, 0])

        return snake

    @staticmethod
    def is_in_range(pos1, pos2):
        """
        Return if tail is in range of head
        :param pos1: Head location
        :param pos2: Tail location
        :return: True if in range, false if not
        """
        return sqrt((pow(pos1[0] - pos2[0], 2)) + pow(pos1[1] - pos2[1], 2)) < 1.5

