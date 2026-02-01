import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="D:/consistency/daily-does-of-coding-consistency-/pgSQL/.evn")

conn = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cursor = conn.cursor()

# -----------------------------
# 1. Insert a single employee
# -----------------------------
insert_query = """
    INSERT INTO employee (id, first_name, last_name)
    VALUES (%s, %s, %s)
"""
cursor.execute(insert_query, (10, 'Arjun', 'Reddy'))

# -----------------------------
# 2. Insert multiple employees
# -----------------------------
employees = [
    (11, 'Meena', 'Kumari'),
    (12, 'Rajesh', 'Varma'),
    (13, 'Sita', 'Devi')
]
cursor.executemany(insert_query, employees)

# -----------------------------
# 3. Update a single employee
# -----------------------------
update_query = """
    UPDATE employee
    SET last_name = %s
    WHERE id = %s
"""
cursor.execute(update_query, ('UpdatedLastName', 10))

# -----------------------------
# 4. Update multiple employees
# -----------------------------
updates = [
    ('NewLast1', 11),
    ('NewLast2', 12),
]
cursor.executemany(update_query, updates)

# -----------------------------
# 5. Delete certain employees
# -----------------------------
delete_query = "DELETE FROM employee WHERE id = %s"
cursor.execute(delete_query, (13,))   # delete one
cursor.executemany(delete_query, [(11,), (12,)])  # delete multiple

# -----------------------------
# 6. Create new tables
# -----------------------------
cursor.execute("""
    CREATE TABLE department (
        dept_id SERIAL PRIMARY KEY,
        dept_name VARCHAR(50) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE project (
        project_id SERIAL PRIMARY KEY,
        project_name VARCHAR(50) NOT NULL
    )
""")

# -----------------------------
# 7. Drop one of the new tables
# -----------------------------
cursor.execute("DROP TABLE project")

# Commit all changes
conn.commit()

# Verify remaining employees
cursor.execute("SELECT * FROM employee")
data = cursor.fetchall()
for d in data:
    print(d)

conn.close()