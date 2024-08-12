import pandas as pd
from WindPy import w
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
本文为基于Wind数据集的CAPM模型测试代码，
直接对股票的收益率和指数的收益率进行回归，
暂时不加入无风险利率
通过stats.linregress函数进行回归分析,得出的beta系数是可用的
stats.linregress提供的是简单线性回归分析，
"""

w.start()
w.isconnected()

cmbc_pct = w.wsd("600036.SH", "pct_chg", "2011-01-01", "2024-07-31", "Period=M", usedf=True)[1]

market_pct = w.wsd("000300.SH", "pct_chg", "2011-01-01", "2024-07-31", "Period=M", usedf=True)[1]

df_capm = pd.DataFrame()
df_capm = pd.concat([market_pct, cmbc_pct], axis=1)

df_capm.index.name = 'Date'
df_capm.columns = ["market_pct", "cmbc_pct"]
df_capm.reset_index(inplace=True)

beta, alpha, r_value, p_value, std_err = stats.linregress(df_capm['market_pct'], df_capm['cmbc_pct'])

print("beta: ", beta)
print("alpha: ", alpha)
print("r_value: ", r_value)
print("p_value: ", p_value)
print("std_err: ", std_err)
print(df_capm)
