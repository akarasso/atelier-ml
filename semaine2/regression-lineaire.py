# import

import numpy as np
import pandas as pd

data = pd.read_csv("database/ex1data1.csv")

data.plot.scatter('population', 'profit')
