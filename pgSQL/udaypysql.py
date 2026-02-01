import psycopg2
import os 
from dotenv import load_dotenv

# Added 'r' for raw string to prevent Windows path errors
load_dotenv(dotenv_path=r"D:\consistency\daily-does-of-coding-consistency-\pgSQL\.evn")

conn = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employee LIMIT 5")
rows = cursor.fetchall()

# Print the results so you can see them!
# if rows:
#     for row in rows:
#         print(row)
# else:
#     print("No records found.")
from tabulate import tabulate

# ... (assume rows and colnames fetched) ...

print(tabulate(rows, headers=colnames, tablefmt="grid"))
cursor.close()
conn.close()