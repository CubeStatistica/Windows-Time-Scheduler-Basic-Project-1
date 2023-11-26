# Basic Project 1 - Script to create and update csv file - Simulate productionization

import datetime as dt
import numpy as np
import pandas as pd

datetime_now = dt.datetime.now()
datetime_now_str = datetime_now.strftime("%Y-%m-%d %H:%M:%S")

# Code to determine the data size. We do not want it to be zero or very large
newdata_size = (datetime_now.second % 22) + 1  # use modulo to now exceed size of 22.

df = pd.DataFrame(
    np.random.randint(0, 100, size=(newdata_size, 4)), columns=list("ABCD")
)
df["datetime"] = datetime_now_str
df["seconds"] = datetime_now.second
