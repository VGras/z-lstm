"""
This module generates a set of data.
"""

import json
import sys
import numpy as np
import pandas as pd

def noisy_sine_generation(time_range, time_step, noise_std) -> dict:
  print('time_range = ', time_range)
  print('time_step = ', time_step)
  print('noise_std = ', noise_std)

  data_dict = {}

  try:
    time = np.arange(0, time_range, time_step)
 
    # Generating data: sine function
    values = np.sin(time) + np.random.normal(scale=noise_std, size=len(time))
    print('Values shape from numpy: ', values.shape)
    
    # Making pandas DataFrame
    # data_df = pd.DataFrame([time, values], index=time, columns=['time','values'])
    data_df = pd.DataFrame(columns=['time','values'])
    data_df['time'] = time
    data_df['values'] = values

    print('Data shape from pandas:')
    print(data_df.shape)
    print('Data frame header:')
    print(data_df.head())

    data_dict["data"] = data_df.to_dict()
  except:
    e = sys.exc_info()[0]
    print(e)
    print('Something went wrong!')

  return data_dict

