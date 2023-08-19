import sys
from shmup.game import game

def main(args=None):
    if args is None: 
        args = sys.args[1:]

    Game = game()
    game.run()

if __name__ == '__main__':
    sys.exit(main())