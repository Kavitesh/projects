import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
print(x)
y = x ** 2

plt.plot(x, y, 'r') 
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
# plt.show()

plt.subplot(1, 8, 7)
plt.plot(x, y, 'r') 
plt.subplot(1, 8, 6)
plt.plot(y, x, 'b') 
plt.show()