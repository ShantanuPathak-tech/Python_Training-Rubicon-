import numpy as np

print("=" * 50)
print("       NUMPY STUDENT MARKS ANALYZER")
print("=" * 50)

# ------------------------------------------------
# 1. CREATE ARRAY
# ------------------------------------------------

marks = np.array([78, 85, 62, 91, 55, 88, 73, 95, 68, 81])

print("\nOriginal Marks:")
print(marks)

# ------------------------------------------------
# 2. ARRAY PROPERTIES
# ------------------------------------------------

print("\n--- Array Properties ---")

print("Number of Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Total Elements:", marks.size)
print("Data Type:", marks.dtype)
print("Memory per Element:", marks.itemsize, "bytes")

# ------------------------------------------------
# 3. INDEXING
# ------------------------------------------------

print("\n--- Indexing ---")

print("First Student:", marks[0])
print("Second Student:", marks[1])
print("Last Student:", marks[-1])

# ------------------------------------------------
# 4. SLICING
# ------------------------------------------------

print("\n--- Slicing ---")

print("First 5 Students:", marks[:5])
print("Last 5 Students:", marks[5:])
print("Students 3 to 7:", marks[2:7])

# ------------------------------------------------
# 5. VECTORIZED OPERATIONS
# ------------------------------------------------

print("\n--- Vectorized Operations ---")

bonus = 5

new_marks = marks + bonus

print("Original Marks:", marks)
print("After Adding Bonus:", new_marks)

# Percentage calculation
percentage = marks / 100 * 100

print("Percentage:", percentage)

# ------------------------------------------------
# 6. STATISTICS
# ------------------------------------------------

print("\n--- Statistics ---")

print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Standard Deviation:", np.std(marks))

# ------------------------------------------------
# 7. FILTERING
# ------------------------------------------------

print("\n--- Filtering ---")

passed = marks[marks >= 40]
top_students = marks[marks >= 80]
failed = marks[marks < 40]

print("Passed Students:", passed)
print("Top Students:", top_students)
print("Failed Students:", failed)

# ------------------------------------------------
# 8. MIN/MAX POSITION
# ------------------------------------------------

print("\n--- Position of Highest/Lowest ---")

highest_position = np.argmax(marks)
lowest_position = np.argmin(marks)

print("Highest Mark Position:", highest_position)
print("Lowest Mark Position:", lowest_position)

print("Highest Mark:", marks[highest_position])
print("Lowest Mark:", marks[lowest_position])

# ------------------------------------------------
# 9. SORTING
# ------------------------------------------------

print("\n--- Sorting ---")

print("Ascending:", np.sort(marks))
print("Descending:", np.sort(marks)[::-1])

# ------------------------------------------------
# 10. ARRAY CREATION FUNCTIONS
# ------------------------------------------------

print("\n--- Array Creation Functions ---")

zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
numbers = np.arange(1, 11)
equal_values = np.linspace(0, 100, 5)

print("Zeros:")
print(zeros)

print("Ones:")
print(ones)

print("Arange:")
print(numbers)

print("Linspace:")
print(equal_values)

# ------------------------------------------------
# 11. RESHAPE
# ------------------------------------------------

print("\n--- Reshape ---")

data = np.arange(1, 13)

matrix = data.reshape(3, 4)

print("Original:")
print(data)

print("3 x 4 Matrix:")
print(matrix)

# ------------------------------------------------
# 12. 2D ARRAY OPERATIONS
# ------------------------------------------------

print("\n--- 2D Array ---")

student_marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 95]
])

print(student_marks)

print("Shape:", student_marks.shape)

print("Total:", np.sum(student_marks))
print("Average:", np.mean(student_marks))

# Row-wise average
print("Row Average:",
      np.mean(student_marks, axis=1))

# Column-wise average
print("Column Average:",
      np.mean(student_marks, axis=0))

# ------------------------------------------------
# 13. RANDOM DATA
# ------------------------------------------------

print("\n--- Random Marks ---")

random_marks = np.random.randint(35, 101, 10)

print("Random Marks:")
print(random_marks)

print("Average:", np.mean(random_marks))
print("Highest:", np.max(random_marks))
print("Lowest:", np.min(random_marks))

print("\n" + "=" * 50)
print("          PROGRAM COMPLETED")
print("=" * 50)