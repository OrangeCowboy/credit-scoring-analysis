# credit-scoring-analysis
This project explores credit risk assessment using real-world credit card default data. The goal is to build a predictive model to determine the likelihood of default, using MySQL for data storage, Python for Analysis and PowerBI for visualisation. The project follows best practices to demonstrate an end-to-end financial DS workflow.

## Dataset
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)
- **Size:** 30,000 rows x 25 columns
- **Description:** Includes demographic, financial and repayment history features for clients of a credit card company

## Data Import Process
- The dataset was importing use MySQL Import Wizard.
- The SQL script to perform this manually is available in 'sql/import.sql'.
- After import, I verified data with:
```sql
SELECT * FROM credit_defaults LIMIT 10;
SELECT COUNT(*) FROM credit_defaults;
```

## Data cleaning Overview
- **Fixed Categorical Variables:**
    - **EDUCATION:** Merge undocumented values ('5, 6 -> 4 (Others)'), replaced '0 -> NaN'.
    - **MARRIAGE:** Replaced '0 -> NaN'.
- **Checked for missing values and anomalies before EDA.**

