import sys
import random
import hashlib

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please provide a name as an argument.")
    else:
        name = args[0]
        print(f"Hello, {name}!")

if __name__ == '__main__':
    main()