class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.marks = {}  # Dictionary to store subject: mark

    def add_mark(self, subject: str, mark: float):
        """Add or update a mark for a specific subject."""
        if 0 <= mark <= 100:
            self.marks[subject] = mark
        else:
            print("Error: Mark must be between 0 and 100.")

    def calculate_average(self) -> float:
        """Calculate the average mark across all subjects."""
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def calculate_grade(self) -> str:
        """Calculate the overall letter grade based on the average mark."""
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        elif avg > 0:
            return "F"
        return "N/A"

    def display_report(self):
        """Print a detailed mark sheet for the student."""
        print("\n" + "=" * 40)
        print(f"STUDENT REPORT - {self.name} (ID: {self.student_id})")
        print("=" * 40)
        if not self.marks:
            print("No marks recorded yet.")
            return

        for subject, mark in self.marks.items():
            print(f"{subject:<20}: {mark:.2f}")

        avg = self.calculate_average()
        grade = self.calculate_grade()
        print("-" * 40)
        print(f"Average Mark         : {avg:.2f}")
        print(f"Overall Grade        : {grade}")
        print("=" * 40)


class StudentMarksSystem:
    def __init__(self):
        self.students = {}  # Dictionary mapping student_id to Student instance

    def add_student(self, student_id: str, name: str):
        """Add a new student to the system."""
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(student_id, name)
            print(f"Student '{name}' added successfully.")

    def add_mark_for_student(self, student_id: str, subject: str, mark: float):
        """Record a subject mark for a given student ID."""
        if student_id in self.students:
            self.students[student_id].add_mark(subject, mark)
            print(f"Mark added for {self.students[student_id].name}.")
        else:
            print(f"Student with ID {student_id} not found.")

    def display_all_students(self):
        """Display summary report for all registered students."""
        if not self.students:
            print("No student records available.")
            return

        print("\n" + "=" * 50)
        print(f"{'ID':<10} {'Name':<20} {'Average':<10} {'Grade':<5}")
        print("=" * 50)
        for s in self.students.values():
            avg = s.calculate_average()
            grade = s.calculate_grade()
            print(f"{s.student_id:<10} {s.name:<20} {avg:<10.2f} {grade:<5}")
        print("=" * 50)


# Example Usage
if __name__ == "__main__":
    system = StudentMarksSystem()

    # 1. Add Students
    system.add_student("S101", "Alice Smith")
    system.add_student("S102", "Bob Johnson")

    # 2. Add Marks for Alice
    system.add_mark_for_student("S101", "Mathematics", 92.5)
    system.add_mark_for_student("S101", "Physics", 88.0)
    system.add_mark_for_student("S101", "Computer Science", 95.0)

    # 3. Add Marks for Bob
    system.add_mark_for_student("S102", "Mathematics", 74.0)
    system.add_mark_for_student("S102", "Physics", 68.5)
    system.add_mark_for_student("S102", "English", 82.0)

    # 4. Display Individual Report
    system.students["S101"].display_report()

    # 5. Display System-Wide Summary
    system.display_all_students()