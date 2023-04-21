#  Write a script that:
# Defines a list of frequencies and a list of amplitudes for the first 20 harmonic components of a triangular wave.
# Creates the corresponding sinusoidal components through a polyphonic Sine object.
# Mix down the components to a mono signal x.
# Plot waveform and spectrum of x.
# Pans x to 2 channels and plays it.
# Note: for a triangular waveform, frequency and amplitude of the kth harmonic are
# fk = (2k+1)f0 
# ak= (-1)^(k-1) /(2k+1)^2

from pyo import *
from mypyoinit import *

freq = 200 # Sets fundamental frequency
high = 20 # Sets the highest harmonic

# List of (odd) harmonic frequencies
harms = [freq * (2*k+1) for k in range(0, high)]
# List of (odd) harmonic amplitudes: (-1)^(k-1) / (2k+1)^2
amps = [0.33 *(-1)**(k-1) / ((2*k+1)**2) for k in range(0, high)]

print(harms)
print(amps)

triang_partials = Sine(freq=harms, mul=amps)  # Creates all sines at once
triang=triang_partials.mix(voices=1) # Mix down into a single signal
triang_out = Pan(triang, outs=2, pan=0.5).out()

Scope(triang)
Spectrum(triang)

s.gui(locals())