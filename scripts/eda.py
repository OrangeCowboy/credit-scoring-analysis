import pandas
from import_pandas import credit_df

print(credit_df.corr())

correlation = credit_df['default_payment_next_month'].corr(credit_df['LIMIT_BAL'])
print(f"The correlation between default_payment_next_month & LIMIT_BAL is:{correlation}")