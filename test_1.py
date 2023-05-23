# for testing py_omnibor
# does nothing useful

import csv
import json
import os 
import datetime
import collections
import re

def main():
    text = "Hello, my email is example@example.com. Please contact me at that address."

    # Define a regular expression pattern to match email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    
    # Use the findall() function to extract all email addresses from the text
    email_addresses = re.findall(pattern, text)
    for email in email_addresses:
        print(email)

if __name__ == '__main__':
    main()


