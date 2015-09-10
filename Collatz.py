#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

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
    assert(i > 0)
    count = 1
    num = i
    while (num > 1):
        if (num % 2) == 0:
            num = (num / 2)
            count = count + 1
        else:
            num = num + (num // 2) + 1
            count += 2
    assert(count > 0)
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
    max = -1
    min = -1
    if i > j:
        max = i
        min = j
    elif j > i:
        max = j
        min = i
    
    else:
        return cycleLength(i)
    for c in range(min, max):
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
