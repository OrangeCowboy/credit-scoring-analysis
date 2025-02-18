import pandas
import sqlalchemy
import pymysql
import matplotlib
import seaborn

print("All packages loaded successfully!")


from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:*****@localhost/credit_scoring", echo=True)

from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())