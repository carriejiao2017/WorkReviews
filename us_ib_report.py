# 
# 按照UCMID






import pandas as pd
us_ib = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\US IB Report_FW43.csv',low_memory=False)
#print(us_ib.head(5))
# # print(us_ib.columns)
# print(us_ib.head(5))
print(us_ib.describe()) #

us_acc_seg_sys = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\Account_segment by SYS.csv',low_memory=False)
us_acc_seg_ucm = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\ULS_Acc_segment by UCMID.csv',low_memory=False)
us_ucm = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\2019-UCM ID.csv',low_memory=False)
us_contract = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\ULS_contract_Report.csv',low_memory=False)



# UCMID作为key值，把us_ucm的值读入us_ib,并赋值给us_ib_report
# us_ib_report = pd.merge(us_ib, us_ucm, on = 'UCM ID', how = "left")
# print(us_ib_report.head(5))
