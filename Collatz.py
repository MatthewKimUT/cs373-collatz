#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

cache = []

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# cycleLength
# ------------

def cycleLength (i):
    """
    i the number whose cycle length is being calculated
    return the cycle length of number i
    """

    for (x, y) in cache:
        if x == i:
            return y
    assert(i > 0)
    count = 1
    num = i
    while (num > 1):
        found = -1
        for(x, y) in cache:
            if(x == num):
                found = y
        if(found != -1):
            count += found - 1 #subtract 1 because the count = 1 from the start of the method is now redundant
            num = 1
        elif (num % 2) == 0:
            num = (num // 2)
            count += 1
        else:
            num = num + (num // 2) + 1
            count += 2
    assert(count > 0)
    cache.append((i, count))
    return count;

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert(i > 0)
    assert(j > 0)
    maxLength = -1
    maxnum = -1
    minnum = -1
    if i > j:
        maxnum = i
        minnum = j
    elif j > i:
        maxnum = j
        minnum = i
    else:
        return cycleLength(i)
    mid = (maxnum // 2) + 1;#algorithm from class cuts down on amount of cycleLength() computations if the smaller of (i, j) is less than j/2 + 1
    start = -1
    if(minnum < mid)
        start = mid;
    else
        start = minnum;
    for c in range(start, maxnum + 1):
        temp = cycleLength(c)
        if temp > maxLength:
            maxLength = temp
    assert(maxLength > 0)
    return maxLength

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
