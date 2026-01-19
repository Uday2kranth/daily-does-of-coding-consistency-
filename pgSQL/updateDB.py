import psycopg2
import os 
from dotenv import load_dotenv
load_dotenv(dotenv_path="D:\consistency\daily-does-of-coding-consistency-\pgSQL\.evn")

conn=psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"))


cursor=conn.cursor()
update=[
    (10,'BhanuPrakash','G'),
    (22,'Akash','D')
]
cursor.executemany("update employee SET id=%s where first_name =%s AND  last_name =%s",update)

conn.commit()
print("IDS Updated Sucessfully!")


# print("\n Here is the Updated table:\n")
cursor.execute("SELECT  * FROM  employee order by id")
rows = cursor.fetchall()
for d in rows:
    print(f"\n{d}\n")
cursor.close()
conn.close()