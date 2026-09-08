import matplotlib.pyplot as plt

print("=" * 60)
print("       MATPLOTLIB STUDENT PERFORMANCE ANALYZER")
print("=" * 60)

# ------------------------------------------------
# DATA
# ------------------------------------------------

subjects = ["Python", "Java", "DBMS", "CN", "Maths"]

marks = [85, 90, 78, 72, 88]

months = ["Jan", "Feb", "Mar", "Apr", "May"]

monthly_marks = [65, 70, 75, 82, 88]

study_hours = [1, 2, 3, 4, 5, 6, 7]

student_marks = [45, 50, 55, 60, 65, 70, 72, 75,
                 78, 80, 82, 85, 88, 90, 95]

# ------------------------------------------------
# 1. LINE CHART
# ------------------------------------------------

plt.figure()

plt.plot(
    months,
    monthly_marks,
    marker="o",
    label="Average Marks"
)

plt.title("Monthly Student Performance")
plt.xlabel("Month")
plt.ylabel("Average Marks")

plt.grid(True)

plt.legend()

plt.show()

# ------------------------------------------------
# 2. BAR CHART
# ------------------------------------------------

plt.figure()

plt.bar(
    subjects,
    marks
)

plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.ylim(0, 100)

plt.show()

# ------------------------------------------------
# 3. HORIZONTAL BAR
# ------------------------------------------------

plt.figure()

plt.barh(
    subjects,
    marks
)

plt.title("Subject-wise Marks")
plt.xlabel("Marks")
plt.ylabel("Subjects")

plt.show()

# ------------------------------------------------
# 4. SCATTER PLOT
# ------------------------------------------------

plt.figure()

plt.scatter(
    study_hours,
    [45, 52, 58, 65, 72, 80, 88]
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid(True)

plt.show()

# ------------------------------------------------
# 5. HISTOGRAM
# ------------------------------------------------

plt.figure()

plt.hist(
    student_marks,
    bins=5
)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

# ------------------------------------------------
# 6. PIE CHART
# ------------------------------------------------

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

students = [
    40,
    25,
    20,
    15
]

plt.figure()

plt.pie(
    students,
    labels=languages,
    autopct="%1.1f%%"
)

plt.title("Programming Language Preference")

plt.show()

# ------------------------------------------------
# 7. MULTIPLE SERIES
# ------------------------------------------------

python_marks = [70, 75, 82, 88]
java_marks = [65, 72, 78, 80]

months2 = ["Jan", "Feb", "Mar", "Apr"]

plt.figure()

plt.plot(
    months2,
    python_marks,
    marker="o",
    label="Python"
)

plt.plot(
    months2,
    java_marks,
    marker="s",
    label="Java"
)

plt.title("Python vs Java Performance")

plt.xlabel("Month")
plt.ylabel("Average Marks")

plt.legend()

plt.grid(True)

plt.show()

# ------------------------------------------------
# 8. SAVE CHART
# ------------------------------------------------

plt.figure()

plt.bar(subjects, marks)

plt.title("Student Subject Performance")

plt.xlabel("Subject")
plt.ylabel("Marks")

plt.savefig(
    "student_performance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully!")
print("File: student_performance.png")

print("=" * 60)
print("             PROGRAM COMPLETED")
print("=" * 60)