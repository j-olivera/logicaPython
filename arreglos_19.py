import numpy as np
import random
teatro = np.zeros([12,30],dtype=int)

for k in range((12*30)):
    i = random.randint(0,11)
    j = random.randint(0,29)
    if teatro[i][j]==0:
        print(f"this places is available, your have the possicion {i+1} {j+1}")
        teatro[i][j]=1
    else:
        print("This place is ocuped, next time!")
