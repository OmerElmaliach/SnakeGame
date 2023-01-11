from math import sqrt
import time


def main():
    snake = setup_snake(3)
    move_snake(snake, 'R', 3)
    move_snake(snake, 'U', 3)


def setup_snake(num):
    snake = []
    for i in range(num):
        snake.append([0, 0])

    return snake


def move_snake(snake, direction, times):
    current_pos, prev_head_pos = [0, 0], [0, 0]
    for i in range(int(times)):
        for k in range(len(snake)):
            if k == 0:
                prev_head_pos = snake[0].copy()
                if direction == 'U':
                    snake[0][0] += 1
                elif direction == 'D':
                    snake[0][0] -= 1
                elif direction == 'L':
                    snake[0][1] -= 1
                elif direction == 'R':
                    snake[0][1] += 1

            elif not is_in_range(snake[k - 1], snake[k]):
                current_pos = snake[k]
                snake[k] = prev_head_pos
                prev_head_pos = current_pos
        print_board(snake)
        time.sleep(0.35)


def print_board(snake):
    for i in range(6, -1, -1):
        for k in range(25):
            if [i, k] in snake:
                print('S', end="")
            else:
                print('x', end="")
        print('')
    print('')


def is_in_range(pos1, pos2):
    """
    Return if tail is in range of head
    :param pos1: Head location
    :param pos2: Tail location
    :return: True if in range, false if not
    """
    return sqrt((pow(pos1[0] - pos2[0], 2)) + pow(pos1[1] - pos2[1], 2)) < 1.5


if __name__ == '__main__':
    main()
