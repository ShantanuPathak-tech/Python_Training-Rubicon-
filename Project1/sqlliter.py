import sqlite3

print("=" * 60)
print("          SQLITE STUDENT DATABASE")
print("=" * 60)

# ------------------------------------------------
# 1. CONNECT DATABASE
# ------------------------------------------------

connection = sqlite3.connect("college.db")

cursor = connection.cursor()

print("\nDatabase connected successfully!")

# ------------------------------------------------
# 2. CREATE TABLE
# ------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (

    id INTEGER PRIMARY KEY,

    name TEXT NOT NULL,

    marks REAL,

    department TEXT
)
""")

connection.commit()

print("Students table created!")

# ------------------------------------------------
# 3. INSERT MULTIPLE RECORDS
# ------------------------------------------------

students = [

    (1, "Amit", 82, "Computer"),

    (2, "Neha", 91, "Computer"),

    (3, "Rahul", 74, "IT"),

    (4, "Pooja", 88, "IT"),

    (5, "Kiran", 95, "Computer")
]

cursor.executemany(
    """
    INSERT OR IGNORE INTO students
    (id, name, marks, department)

    VALUES (?, ?, ?, ?)
    """,

    students
)

connection.commit()

print("Students inserted!")

# ------------------------------------------------
# 4. READ ALL RECORDS
# ------------------------------------------------

print("\n--- ALL STUDENTS ---")

cursor.execute(
    "SELECT * FROM students"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

# ------------------------------------------------
# 5. WHERE CONDITION
# ------------------------------------------------

print("\n--- MARKS >= 80 ---")

cursor.execute(
    """
    SELECT name, marks
    FROM students
    WHERE marks >= ?
    """,

    (80,)
)

rows = cursor.fetchall()

for row in rows:
    print(row)

# ------------------------------------------------
# 6. ORDER BY
# ------------------------------------------------

print("\n--- SORTED BY MARKS ---")

cursor.execute(
    """
    SELECT name, marks
    FROM students
    ORDER BY marks DESC
    """
)

rows = cursor.fetchall()

for row in rows:
    print(row)

# ------------------------------------------------
# 7. FETCHONE
# ------------------------------------------------

print("\n--- FIND STUDENT ID 2 ---")

cursor.execute(
    """
    SELECT *
    FROM students
    WHERE id = ?
    """,

    (2,)
)

student = cursor.fetchone()

if student:

    print("Student Found:", student)

else:

    print("Student Not Found")

# ------------------------------------------------
# 8. UPDATE
# ------------------------------------------------

print("\n--- UPDATE ---")

cursor.execute(
    """
    UPDATE students

    SET marks = ?

    WHERE id = ?
    """,

    (96, 1)
)

connection.commit()

print("Amit's marks updated!")

# ------------------------------------------------
# 9. VERIFY UPDATE
# ------------------------------------------------

cursor.execute(
    """
    SELECT *
    FROM students
    WHERE id = ?
    """,

    (1,)
)

print(cursor.fetchone())

# ------------------------------------------------
# 10. DELETE
# ------------------------------------------------

print("\n--- DELETE ---")

cursor.execute(
    """
    DELETE FROM students

    WHERE id = ?
    """,

    (3,)
)

connection.commit()

print("Student ID 3 deleted!")

# ------------------------------------------------
# 11. DISPLAY FINAL DATA
# ------------------------------------------------

print("\n--- FINAL DATA ---")

cursor.execute(
    "SELECT * FROM students"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

# ------------------------------------------------
# 12. TRANSACTION + ROLLBACK
# ------------------------------------------------

print("\n--- TRANSACTION TEST ---")

try:

    cursor.execute(
        """
        UPDATE students

        SET marks = ?

        WHERE id = ?
        """,

        (100, 2)
    )

    connection.commit()

    print("Transaction successful!")

except sqlite3.Error as error:

    connection.rollback()

    print("Database Error:", error)

# ------------------------------------------------
# 13. FINAL RECORDS
# ------------------------------------------------

print("\n--- FINAL STUDENT RECORDS ---")

cursor.execute(
    """
    SELECT *
    FROM students
    ORDER BY marks DESC
    """
)

for row in cursor.fetchall():

    print(
        "ID:", row[0],
        "| Name:", row[1],
        "| Marks:", row[2],
        "| Department:", row[3]
    )

# ------------------------------------------------
# 14. CLOSE CONNECTION
# ------------------------------------------------

connection.close()

print("\nDatabase connection closed!")

print("=" * 60)
print("             PROGRAM COMPLETED")
print("=" * 60)