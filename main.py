from pynput.keyboard import Listener
import snake

snake = snake.Snake(3)


def main():
    with Listener(on_press=event_listener) as listener:
        listener.join()


def event_listener(key):
    switch = {
        key.up: 'U',
        key.down: 'D',
        key.left: 'L',
        key.right: 'R'
    }

    snake.move_snake(switch.get(key, "None"), 1)


if __name__ == '__main__':
    main()
