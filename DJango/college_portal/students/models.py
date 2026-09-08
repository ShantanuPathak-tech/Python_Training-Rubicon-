from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.FloatField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    # NEW FUNCTION: Auto-calculate letter grade
    def get_grade(self):
        if self.marks >= 90:
            return 'A+'
        elif self.marks >= 80:
            return 'A'
        elif self.marks >= 70:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        elif self.marks >= 50:
            return 'D'
        else:
            return 'F'