import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Housing.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())