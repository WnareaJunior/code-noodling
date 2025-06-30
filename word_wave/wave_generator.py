import math
import time
import numpy as np


print('\n'*4)
print('*****Make a Wave *****')
print('Welcome to Wave Maker!')
name = input('What is your name? ')
print('Hello, ' + name + '! Let\'s create a wave together!')
def sine_wave(x):
    """Generate a sine wave pattern."""
    return int(21+ 20 * ( np.sin(x/20)))
def wave_with_name(x):
    if( x/len(name)<=1):
        return name[0:x]
    else:
        return name*(int(x/len(name)))+ name[0:x % len(name)]

for i in range(1000):
    time.sleep(0.01)  # Adjust the speed of the wave
    print(wave_with_name(sine_wave(i)))