import psycopg2
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="D:\consistency\daily-does-of-coding-consistency-\pgSQL\.evn")



conn= psycopg2.connect(
	database=os.getenv("DB_NAME"),
	user=os.getenv("DB_USER"),
	password=os.getenv("DB_PASSWORD"),
	host=os.getenv("DB_HOST"),
	port=os.getenv("DB_PORT")
)

# print("DB_USER:", os.getenv("DB_USER"))
# print("DB_PASSWORD:")
cursor = conn.cursor()

update_query="""update employee set id =%s where first_name=%s"""
cursor.execute(update_query,(39,'UdayKranth'))
conn.commit()
cursor.execute("SELECT  * FROM  employee")

data = cursor.fetchall()
for d in data:
    print(f"\n[{d}]\n")
print(data)
conn.close()
