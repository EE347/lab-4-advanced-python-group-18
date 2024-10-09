import numpy as np


x = np.linspace(0, 10, 101)
print(x)

# Generate sine and cosine waves
sin_wave = np.sin(x)
cos_wave = np.cos(x)

# Save the arrays to files
np.save('/home/pi/ee347/lab-4-advanced-python-group-18/task7_sin.npy', sin_wave)
np.save('/home/pi/ee347/lab-4-advanced-python-group-18/task7_cos.npy', cos_wave)

# Verifying by loading and printing
loaded_sin_wave = np.load('/home/pi/ee347/lab-4-advanced-python-group-18/task7_sin.npy')
loaded_cos_wave = np.load('/home/pi/ee347/lab-4-advanced-python-group-18/task7_cos.npy')

print('Sine wave:', loaded_sin_wave)
print('Cosine wave:', loaded_cos_wave)