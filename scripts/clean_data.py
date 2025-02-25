import pandas
from import_pandas import credit_df

credit_df['EDUCATION'] = credit_df['EDUCATION'].replace(0, pandas.NA)
credit_df['EDUCATION'] = credit_df['EDUCATION'].replace([5, 6], 4)

credit_df['MARRIAGE'] = credit_df['MARRIAGE'].replace(0, pandas.NA)


print(credit_df['MARRIAGE'].value_counts())
print(credit_df['EDUCATION'].value_counts())

print(credit_df['MARRIAGE'].isnull().sum())
print(credit_df['EDUCATION'].isnull().sum())
