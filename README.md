# credit-scoring-analysis
This project explores credit risk assessment using real-world credit card default data. The goal is to build a predictive model to determine the likelihood of default, using MySQL for data storage, Python for Analysis and PowerBI for visualisation. The project follows best practices to demonstrate an end-to-end financial DS workflow.

## Data Import Process
- The dataset was importing use MySQL Import Wizard.
- The SQL script to perform this manually is available in 'sql/import.sql'.
- After import, I verified data with:
```sql
SELECT * FROM credit_defaults LIMIT 10;
SELECT COUNT(*) FROM credit_defaults;
