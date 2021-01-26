from django.db import models
# Create your models here.


class Student(models.Model):
    GRADE = (
        ('A+', 'A+'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    firstname = models.CharField(max_length=1000, blank=False, null=False)
    lastname = models.CharField(max_length=1000, blank=False, null=False)
    number = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=False, default=0)
    grade = models.CharField(max_length=150, null=True,
                             blank=True, choices=GRADE, default=GRADE[0][0])
    image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return self.firstname


class StudentClass(models.Model):
    studentName = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=False, blank=False)
    studentclass = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=False, default=0)

    def __str__(self):
        return self.studentName.firstname
