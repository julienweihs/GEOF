import matplotlib.pyplot as plt
# to install latest release using pip:
# >> pip install matplotlib
# or
# if using a Conda package (on 'base' or other virtual environment):
# >> conda install matplotlib

import numpy as np
# to install latest release using pip:
# >> pip install numpy
# or
# if using a Conda package (on 'base' or other virtual environment):
# >> conda install numpy

x = np.array([2,6,8,3,1,4,5,3])
y=np.array([1,4,5,2,7,9,6,4])
z=np.array([0,4,5,3,7,10,6,4])

plt.plot(x, label='x')
plt.plot(y, label='y')
plt.plot(z, label='z')

plt.legend()
plt.show()
