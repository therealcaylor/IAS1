# Creates a sinusoid with the following properties:
# - oscillating around the value 1 (rather than 0).
# -  with amplitude controllable through ctrl(), between ±0.1 and ±0.8 around 1.
# - with frequency in the range [1-10] Hz.
# Creates and play a signal which is the product a sinusoid (oscillating at audio rates) and the previous one.
# Plots waveform and spectrum of this signal. Note: this should produce an “amplitude-modulation” effect.

import mypyoinit
from pyo import *

modulator = Sine(freq=2, add=1)
mymaplist=[SLMap(0.5, 10, "lin", "freq", 2),SLMap(0.1, 0.8, "lin", "mul", 0.5)]
modulator.ctrl(map_list=mymaplist, title="'Slow' sinusoid (LFO)")
signal = Sine(400)
signal.ctrl(title="signal")
result = (modulator*signal).out()
Scope(result)
Spectrum(result)
mypyoinit.s.gui()

