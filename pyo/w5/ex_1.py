# Write a script that
# Reads n frequency values (in Hertz) from a list of numbers
# Creates n sinusoids, each with one frequency from the list
# Plays all the sinusoids simultaneously
import mypyoinit
from pyo import *
arrFreq = [440,441]
arrSines = [Sine(i).out() for i in arrFreq]
mypyoinit.s.gui(locals())
