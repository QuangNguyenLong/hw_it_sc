import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

def CodeRate(delta, f, x):
  entropy_x = np.trapezoid(f(x), x)
  return entropy_x - np.log2(delta)

def Distortion(delta, f):
  K = range(-100, 100)
  U = np.linspace(- delta / 2, delta / 2, 1000)
  S = np.sum([[u**2 * f(u + (k + 1/2) * delta) for u in U] for k in K], axis=0)

  D = np.trapezoid(S, U)
  return D


def mid_tread_quantize(X : list, delta) -> tuple[list, list]:
    indices = np.floor(X / delta)
    qx = delta * (indices + 0.5)
    return qx, indices

def mid_tread_deindex(indices : list, delta) -> list:
    return delta * (indices + 0.5)

def mid_riser_quantize(X : list, delta) -> tuple[list, list]:
    indices = np.floor(X / delta + 0.5)
    qx = delta * indices
    return qx, indices

def mid_riser_deindex(indices : list, delta) -> list:
    return delta * indices

sr, data = wavfile.read("assets/audio.wav")

data = np.array(data, dtype=np.float32).mean(axis=1) # mono, range [-32768, 32767]

# scaled_data = (data / 32768.0 + 1) / 2.0 # range [0, 1]

delta = 0.5

scaled_delta = delta * 32768.0

quantized_data, indices = mid_tread_quantize(data, scaled_delta)


print(indices[1231:1240])

