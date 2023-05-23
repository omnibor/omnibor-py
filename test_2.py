# for testing py_omnibor
# REQUIRES a pip install of the requests library
#     if you do not pip install, py_omnibor will note that something was not installed
#     but otherwise works
# does nothing useful
import sys
import random
import hashlib
import requests

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please provide a name as an argument.")
    else:
        name = args[0]
        print(f"Hello, {name}!")

if __name__ == '__main__':
    main()