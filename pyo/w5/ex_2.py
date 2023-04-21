# Reads n “notes” from a list of tuples (each tuple is made by two numbers: frequency in Hertz, duration in seconds)
# Plays the melody of the n notes using sinusoids (each note starts immediately after the previous one)
# Hint: check the documentation of the out() method in the Sine class, particularly its optional arguments

import mypyoinit
from pyo import *
arr = [(400,1),(600,1),(700,1),(400,1)]
arrSines = []
totSecs = 0
for i in range(len(arr)):
        arrSines.append(Sine(freq=arr[i][0]).out(dur=arr[i][1], delay=totSecs))
        totSecs += arr[i][1]
mypyoinit.s.gui(locals())


