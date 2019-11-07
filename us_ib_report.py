import pandas as pd
us_ib = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\US IB Report_FW43.csv',low_memory=False)
print(us_ib.head(5))
print(us_ib.columns)
print(us_ib['Status'].unique)