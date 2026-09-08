import pandas as pd

# 1. Create DataFrame
data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Department": ["Computer", "IT", "Computer", "IT", "Computer"],
    "Marks": [85, 72, 91, 68, 78]
}

df = pd.DataFrame(data)

print("Complete Data:")
print(df)

# 2. First records
print("\nFirst 3 records:")
print(df.head(3))

# 3. Last records
print("\nLast 2 records:")
print(df.tail(2))

# 4. Information
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

# 5. Statistics
print("\nStatistics:")
print(df.describe())

# 6. Select one column
print("\nStudent Names:")
print(df["Name"])

# 7. Filter students
print("\nStudents with marks >= 75:")
print(df[df["Marks"] >= 75])

# 8. Multiple conditions
print("\nComputer students with marks >= 80:")
print(df[(df["Department"] == "Computer") &
         (df["Marks"] >= 80)])

# 9. Add Bonus column
df["Bonus"] = 5

# 10. Calculate final marks
df["FinalMarks"] = df["Marks"] + df["Bonus"]

print("\nUpdated Data:")
print(df)

# 11. Create Grade
def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "F"

df["Grade"] = df["FinalMarks"].apply(calculate_grade)

print("\nData with Grade:")
print(df)

# 12. Sorting
print("\nStudents sorted by marks:")
print(df.sort_values("FinalMarks", ascending=False))

# 13. GroupBy
print("\nDepartment average:")
print(df.groupby("Department")["FinalMarks"].mean())

# 14. Find topper
topper = df.loc[df["FinalMarks"].idxmax()]

print("\nTopper:")
print(topper)

# 15. Save to CSV
df.to_csv("student_result.csv", index=False)

print("\nCSV file created successfully!")