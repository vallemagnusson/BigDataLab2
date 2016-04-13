#!/usr/bin/env python

import sys
import ujson
import time

# input comes from STDIN (standard input)
dictionary = ["han","hon","den","det","denna","denne","hen"]
start = time.time()
for line in sys.stdin:
    # print line
    # remove leading and trailing whitespace
    line = line.strip()
    try:
        data = ujson.loads(line)
        # split the line into words
        ###words = line.split()
        # print data  
        words = data["text"].lower().split()
        # print words
        # increase counters
        for word in words:
            if word in dictionary:
                # write the results to STDOUT (standard output);
                # what we output here will be the input for the
                # Reduce step, i.e. the input for reducer.py
                #
                # tab-delimited; the trivial word count is 1
                print '%s\t%s' % (word, 1)
    except Exception:
        pass