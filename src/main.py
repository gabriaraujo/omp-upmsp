from functions import *
import sys


def main():
    file = read_file(sys.argv[1])

    write_file(sys.argv[2], solver(file))
    # file_print(file)


if __name__ == '__main__':
    main()
