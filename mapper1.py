#!/usr/bin/env python

#This is a simple mapper script from Michael Noll's
# blog post: http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into individual words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT
        # what we output here will be the input for the
        # Reduce step (reducer1.py)
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)
        
