from lib import *
import sys

def main():
    file = read_file(sys.argv[1])
    for f in file: print(f)

if __name__ == '__main__':
    main()
