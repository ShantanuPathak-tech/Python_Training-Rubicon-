# file = open("file.txt", "w")
# file.write("Name: Rahul\n")
# file.write("Marks: 85\n")
# file.append("Name: Gandu\n")

# file.close()

import os

filename = "student.txt"

try:
    with open(filename, "w") as file:
        file.write("Name: Shantanu\n")
        file.write("Course: Python\n")
        file.write("Age: 21\n")
        
    print("1. file created successfully")
    
    # Write Operation
    with open(filename, "w") as file:
        file.write("Name: Yogesh\n")
        file.write("Course: Python Django\n")
        file.write("City: Pune\n")
        
    print("2. Data written successfully")
    
    #3. Read Complete File
    with open(filename, "w") as file:
        data = file.read()
        
    print("\n Complete File Data")
    print(data); 
    
    #4. Read the line
    with open(filename, "w") as file:
        line = file.readline()
        
    print("1. First line:")
    print(line) 
    
    #5. Read all lines
    with open(filename, "w") as file:
        lines = file.readlines()
        
    print("5. All lines")
    print(lines)
    
    #6. Append Operations
    with open(filename, "w") as file:
        file.write("Technology : Python\n")
        file.write("Experience: 2-3 years\n")
        
    print("6. Data Appended successfully")
    
    #7. Read Update file
    with open(filename, "r") as file:
        print("\n Updated file Data")
        print(file.read())
        
    #8. Check file Exists
    if os.path.exists(filename):
        print("8. File Exists");
        
    #9. File Information
    size = os.path.getsize(filename)
    print("9. File size", size, "bytes");
    
except FileExistsError:
    print("File already exists");
    
except FileNotFoundError:
    print("File not Found")
    
except Exception as e:
    print("Error", e);
    
#10. Delete file
if os.path.exists(filename):
    os.remove(filename)
    print("10. File Deleted successfully");
    
    
    
        
        
    
    
