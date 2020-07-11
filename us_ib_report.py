# 
# 按照UCMID






import pandas as pd
us_ib = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\US IB Report_FW43.csv',low_memory=False)
#print(us_ib.head(5))
#print(us_ib.columns)
# print(us_ib.head(5))
# print(us_ib.describe()) 

us_acc_seg_sys = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\Account_segment by SYS.csv',low_memory=False)
us_acc_seg_ucm = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\ULS_Acc_segment by UCMID.csv',low_memory=False)
us_ucm = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\2019-UCM ID.csv',low_memory=False)
us_contract = pd.read_csv(r'C:\Users\503047919\Desktop\python\US IB Report\ULS_contract_Report.csv',low_memory=False)

# print(us_ucm.columns)
# print(us_acc_seg_ucm.columns)

#删除us_ucm的后面几列
us_ucm.drop(['BA', 'BA.1', 'BA.2', 'BA.3', 'BA.4', 'BA.5', 'BA.6'], axis = 1, inplace = True)
#UCMID作为key值，把us_ucm的值读入us_ib,并赋值给us_ib_report

us_ib_report = pd.merge(us_ib, us_ucm, on = 'UCM ID', how = "left")
# print(us_ib_report.head(5))

us_ib_report = pd.merge(us_ib_report, us_acc_seg_sys, on = 'System ID', how = "left")
# print(us_ib_report.head(5))

# 把未被sys_seg的部分通过UCMID_seg来补充完整
us_ib_report = pd.merge(us_ib_report, us_acc_seg_ucm, left_on = 'UCM ID', right_on = 'UCMID', how = "left")
# print(us_ib_report.head(5))

# 把contract表按照合同结束时间排序，再V到us_ib_report上面
# print(us_contract.columns)
print(us_contract['End'])