import akshare
import arrow


import pandas as pd

# 创建一个简单的DataFrame
df = pd.DataFrame({
    'Value1': [0.1234, 0.5678, 0.9012],
    'Value2': [0.3456, 0.7890, 0.1234]
})

# 使用'{:,.2%}'格式化样式
styled_df = df.style.format('{:,.2%}')
output = styled_df.to_string()
# 显示格式化后的DataFrame
print(type(output))
print()