#Tuple
coordinates = (40.7128, -74.0060)# Tuple named "coordinates is created"

latitude = coordinates[0];#latitude variable accesees the 1st element of tuple
longitude = coordinates[1];#longitude variable accesees the 2nd element of tuple

lat, lon = coordinates
has_lat = 40.7129 in coordinates
print(has_lat);


# 1. Dictionary Definition
students = {"name": "Shantanu", "Rollno": 23, "age": 21}

# 2. Accessing existing values
students_name = students["name"]       # Returns "Shantanu"
students_age = students.get("age")     # Returns 21 (get() avoids errors if key doesn't exist)

# 3. Operations
students["email"] = "shantanu@ai.com"  # Adds a new key-value pair (Updated example email)
students["age"] = 26                   # Updates an existing value from 21 to 26
del students["Rollno"]                 # Removes "Rollno"

# 4. HOW TO ACCESS EMAIL
# Method 1: Using square brackets []
email_method1 = students["email"]

# Method 2: Using the .get() method (recommended to prevent errors)
email_method2 = students.get("email")

# Printing the results
print(f"Name: {students_name}")
print(f"Age (before update): {students_age}")
print(f"Email (Method 1): {email_method1}")
print(f"Email (Method 2): {email_method2}")
print(f"Updated Dictionary: {students}")



# Sets operations
# 1. Creating the student sets
# Students enrolled in Math class
math_students = {"Alice", "Bob", "Charlie", "David"}

# Students enrolled in Science class
science_students = {"Charlie", "David", "Emma", "Frank"}

print(f"Math Students: {math_students}")
print(f"Science Students: {science_students}\n")


# 2. UNION: All unique students across both classes
# Method 1: Using the .union() method
union_method = math_students.union(science_students)
# Method 2: Using the | operator
union_operator = math_students | science_students

print("--- Union ---")
print(f"Using method:   {union_method}")
print(f"Using operator: {union_operator}\n")


# 3. INTERSECTION: Students enrolled in BOTH classes
# Method 1: Using the .intersection() method
intersection_method = math_students.intersection(science_students)
# Method 2: Using the & operator
intersection_operator = math_students & science_students

print("--- Intersection ---")
print(f"Using method:   {intersection_method}")
print(f"Using operator: {intersection_operator}\n")


# 4. DIFFERENCE: Students in Math but NOT in Science
# Method 1: Using the .difference() method
diff_method = math_students.difference(science_students)
# Method 2: Using the - operator
diff_operator = math_students - science_students

print("--- Difference (Math - Science) ---")
print(f"Using method:   {diff_method}")
print(f"Using operator: {diff_operator}")
