LOAD DATA INFILE 'C:\Users\afgha\credit-scoring-analysis\data\default of credit card clients.csv'
INTO TABLE credit_defaults
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;