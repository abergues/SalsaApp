
"""
# Use time series to find the beat in music
The beat should be used to select images and keypoints for notation


1. Read the csv file with info.
2. Convert to timeseries
3. find the length of cycle
4. select the 0 movement point for the feet, as the "Beat"
5. Mark this in the data
6. save csv data

"""

#### AUTHENTICATE USER/APP on Google
import pandas as pd
import requests
import csv
from pathlib import Path
import os
from os.path import exists, join, basename, splitext


# https://drive.google.com/file/d/12v8kJJp_Bvsz3xJMc3olvl-3Wce3_Acb/view?usp=sharing
url = wget('https://drive.google.com/file/d/12v8kJJp_Bvsz3xJMc3olvl-3Wce3_Acb/view?usp=sharing')
print(url)
openpose_df = pd.read_csv(url)
openpose_df
