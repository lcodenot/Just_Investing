import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
data_Returns = pd.read_excel('Returns.xlsx', header = 0).transpose()


data_Returns_Total = data_Returns+1

data_Returns_Summary = data_Returns

data_Returns_Summary['STD DEV'] = data_Returns.std(axis = 1,numeric_only = float)

data_Returns_Summary['Count'] = data_Returns.count(axis = 1)

data_Returns_Summary['Total Return'] = (data_Returns_Total.prod(axis = 1))

data_Returns_Summary['Average Return'] = data_Returns['Total Return'].pow(1/data_Returns['Count'])

(data_Returns_Summary[['Count','Total Return','Average Return','STD DEV']].sort_index()).to_csv('Simplified_Returns')
