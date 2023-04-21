from pyo import *

# Starts and boots pyo audio server
s = Server(buffersize=1024,duplex=0) # if needed, pass argument duplex = 0
#s.setOutputDevice(14)# if needed, select audio device
s.setAmp(0.1)
s.boot()

