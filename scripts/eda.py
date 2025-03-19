import pandas
from import_pandas import credit_df

print(credit_df.corr())


var1 = 'default_payment_next_month'
var2 = 'LIMIT_BAL'
var3 = 'EDUCATION'

correlation = credit_df[var1].corr(credit_df[var2])
print(f"The correlation between {var1} & {var2} is:{correlation}")

correlation = credit_df[var1].corr(credit_df[var3])
print(f"The correlation between {var1} & {var3} is:{correlation}")

credit_df['Total_Paid'] = credit_df[['PAY_AMT1','PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']].sum(axis=1)
credit_df['Total_Bill'] = credit_df[['BILL_AMT1','BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']].sum(axis=1)
credit_df['DTI_debt'] = credit_df['Total_Bill'] / credit_df['Total_Paid']

print((credit_df['Total_Paid'] == 0).value_counts())            # 1432 true, 5% paid $0, need to think of including 0's
