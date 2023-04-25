import mypyoinit
from pyo import *

square = LFO(freq=220, type=2)
square.ctrl(title="square")
tremolo = LFO(2, type=3, mul=0.2, add = 1) # ... or use the range method
freqmap = SLMap(0.1, 5, "lin", "freq", 0.5)
typemap = SLMap(0, 7, "lin", "type", 7, res='int', dataOnly=True)
mulmap = SLMap(0.1, 0.9, "lin", "mul", 0.5)
tremolo.ctrl(title="Tremolo", map_list=[freqmap, typemap, mulmap])
sig = square*tremolo
r = Reson(sig, freq=[1000, 1200, 1400] , q=30)
r.ctrl(title="Resonant filters")
lp = ButLP(r, 2000).out()
lp.ctrl()
mypyoinit.s.gui(locals())

