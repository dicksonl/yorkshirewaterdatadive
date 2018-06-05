import numpy as np
import pandas as pd
import tensorflow as tf

df = pd.read_csv("./data/df_31.csv", parse_dates=['Date'],index_col='Date', infer_datetime_format=True)
