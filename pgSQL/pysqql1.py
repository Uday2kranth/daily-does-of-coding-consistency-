import psycopg2
import os 
from dotenv import load_dotenv
# load_dotenv(dotenv_path="D:\consistency\daily-does-of-coding-consistency-\pgSQL\.evn")
load_dotenv(dotenv_path="D:\consistency\daily-does-of-coding-consistency-\pgSQL\.evn")


# conn=psycopg2.connect(
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_USER"),
#     host=os.getenv("DB_HOST"),
#     port=os.getenv("DB_PORT")
# )

conn= psycopg2.connect(
	database=os.getenv("DB_NAME"),
	user=os.getenv("DB_USER"),
	password=os.getenv("DB_PASSWORD"),
	host=os.getenv("DB_HOST"),
	port=os.getenv("DB_PORT")
)
#alternavtive to previous copnnection script method is ulr like below 
# conn = psycopg2.connect(os.environ["DATABASE_URL"])
cursor = conn.cursor()


cursor.execute("SELECT * FROM titanic LIMIT 5")
rows=cursor.fetchall()
for row in rows:
    print(f"\n\n[{row}]\n\n")
    # print(row)
print(f"\nthis 5 rows from titanic table in my db:\n{rows}")
cursor.close()
conn.close()