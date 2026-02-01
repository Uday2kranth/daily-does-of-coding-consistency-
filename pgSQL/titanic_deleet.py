import psycopg2
import os
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv(dotenv_path ="D:\consistency\daily-does-of-coding-consistency-\pgSQL\.evn")
conn=psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_port"))

cursor=conn.cursor()
delete_query=""" delete from titanic where PassengerId=%s """
cursor.execute(delete_query,(902309,))
conn.commit()


cursor.execute("select * from titanic order by PassengerId desc limit 6")
conn.commit()
rows= cursor.fetchall()
for row in rows:
    print(f"\n[{row}]\n")
cursor.close()
conn.close()

