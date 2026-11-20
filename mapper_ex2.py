#!/usr/bin/env python3
#!/usr/bin/env python
"""mapper.py"""

import sys

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT
        # this output will be input for reducer.py
        for word in words:
            word = word.lower().rstrip(',.')
            if word:
                print('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()
