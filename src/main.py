from src.functions import *
import sys


def main():
    file = read_file(sys.argv[1])
    debug_print(file)


if __name__ == '__main__':
    main()
