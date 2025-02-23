import pandas
from connect_mysql import engine        # engine is a local object ∴ import
print(engine)

credit_df = pandas.read_sql('SELECT * FROM credit_defaults', engine)

print(credit_df)
print(credit_df.info())
print(credit_df.describe())
print(credit_df.duplicated().sum)       # no duplicates
print(credit_df[credit_df < 0].sum)     # no negative values where we don't want


for v in credit_df.columns:
    print(f"\nColumn: {v}")
    print(credit_df[v].unique())


for v in credit_df.columns:
    print(credit_df[v].value_counts())