import pandas
import sqlalchemy
import pymysql
import matplotlib
import seaborn

print("All packages loaded successfully!")


from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:SQL997s*@localhost/credit_scoring", echo=True)

from sqlalchemy import text

def main():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 'hello world'"))
        print(result.all())

if __name__ == "__main__":
    main()        