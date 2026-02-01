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
insert_query=""" insert into titanic(PassengerId,Survived,Name,Pclass,Sex) values(%s,%s,%s,%s,%s)"""
# CREATE TABLE uday_titanic (
#     PassengerId INTEGER PRIMARY KEY,
#     Survived INTEGER,
#     Pclass INTEGER,
#     Name VARCHAR(255),
#     Sex VARCHAR(10),
#     Age NUMERIC,
#     SibSp INTEGER,
#     Parch INTEGER,
#     Ticket VARCHAR(50),
#     Fare NUMERIC,
#     Cabin VARCHAR(50),
#     Embarked VARCHAR(5)
cursor.execute(insert_query,(902303,1,'M.kiran',1,'male'))
entries=[(902309,1,'M.kiran',1,'male'),
         (902304,1,'aludu tarun',1,'male'),
         (902305,1,'pini Shivani',1,'female'),
         (902306,1,'babhai sai kiran',1,'male')]
cursor.executemany(insert_query,entries)
conn.commit()

rows= cursor.fetchall()
for row in rows:
    print(f"\n[{row}]\n")
cursor.close()
conn.close()