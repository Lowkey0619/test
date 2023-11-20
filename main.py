import numpy as np
import matplotlib.pyplot as plt

# Create a sine wave
t = np.arange(0, 2*np.pi, 0.01)
signal = np.sin(t)

# Plot the sine wave
plt.plot(t, signal)
plt.title('Sine Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
