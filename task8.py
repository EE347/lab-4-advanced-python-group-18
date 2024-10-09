import numpy as np
import matplotlib.pyplot as plt

# Load the saved .npy files
sin_wave = np.load('/home/pi/ee347/lab-4-advanced-python-group-18/task7_sin.npy')
cos_wave = np.load('/home/pi/ee347/lab-4-advanced-python-group-18/task7_cos.npy')

# Generate x values again
x = np.linspace(0, 10, 101)

# Plot the sine and cosine waves
plt.plot(x, sin_wave, label='Sine Wave')
plt.plot(x, cos_wave, label='Cosine Wave')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Sine and Cosine Waves')
plt.legend()
plt.show()