import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.linspace(10, 20, 20)
data1 = np.linspace(20, 30, 20)
data = pd.DataFrame({"x": data, "y": data1})

# Correct the typo and ensure matplotlib is used
data.plot(kind="scatter", x="x", y="y")
plt.show()
