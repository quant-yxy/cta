import pandas as pd
import numpy as np
from get_ic import *


data=pd.read_csv(r'D:\data\main_contract_15-23_all'+'\\main_contract_15-23_all.csv',index_col=0).set_index('datetime')
data=data.sort_index()
n=30
df1 = data.groupby('code')['ret'].rolling(window=n).apply(lambda x: (x + 1).prod() - 1).reset_index()
df1.columns = ['code', 'datetime', f'mom_{n}']
data = data.reset_index().merge(df1, on=['datetime', 'code']).sort_values(['code', 'datetime'])
ic = ic_group(data, f'mom_{n}', lag=0)
print_ic_plot(ic, 252, f'mom_{n}')
