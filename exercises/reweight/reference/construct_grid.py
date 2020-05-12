import numpy as np
import matplotlib.pyplot as plt

points = 200
x = np.linspace(-2,2,points)

print('#! FIELDS time d1.x d1.y')
time = 0.0
for p1 in range(points):
    for p2 in range(points):
        print(time,x[p1],x[p2])
        time = time + 1.0

np.savetxt('bins_x.dat',x)
np.savetxt('bins_y.dat',x)
