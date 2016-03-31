import cmath
import numpy
import scikits.audiolab as audio
import matplotlib.pyplot as plt

norm = lambda x: cmath.polar(x)[0]

(inputSignal, samplingRate, bits) = audio.wavread('no_tree_ent.wav')

transformedSignal = numpy.fft.fft(inputSignal)
freq = numpy.fft.fftfreq(len(inputSignal),d=1.0/samplingRate)
plt.plot(freq,[norm(x) for x in transformedSignal])
plt.show()
