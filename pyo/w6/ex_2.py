import mypyoinit
from pyo import *
path = './pianokeys-meral_amp_mono.wav'
audio = SfPlayer(path=path, speed=[0.5,1,2], loop=True)
audio.ctrl("audio")
filt = MoogLP(audio,1000)

pink = PinkNoise()
pink_mod = Sine(freq=0.1, mul=0.5, add=0.1)
freqMap = SLMap(min = 0.05,max = 0.2, name="freq")
mulmap = SLMap(0.1, 0.9, "lin", "mul", 0.5)
pink_mod.ctrl(title="Noise envelope", map_list=[freqMap, mulmap])
noise =( pink*pink_mod)

p = Pan(filt.mix(1)+noise, pan=0.5).out()

mypyoinit.s.gui(locals())