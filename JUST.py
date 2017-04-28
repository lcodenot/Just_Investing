import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

df_returns = pd.read_csv('Simplified_Returns', sep = ',', index_col = 0)

df_scores = pd.read_excel('Scores.xls', header = 0, index_col = 0)

df_returns.index = df_returns.index.map(unicode) 
df_scores.index = df_scores.index.map(unicode) 

print type(df_returns.index)
print type(df_scores.index)

df = pd.concat([df_returns, df_scores], axis=1, join='inner')


print df.head()


