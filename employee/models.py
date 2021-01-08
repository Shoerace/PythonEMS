from django.db import models

# Create your models here.
class Position(models.Model):
    Title=models.CharField(max_length=50)

    def __str__(self):
       return self.Title

class Employee(models.Model):
    FullName=models.CharField(max_length=100)
    Emp_Code=models.CharField(max_length=10)
    Mobile=models.CharField(max_length=10)
    Position=models.ForeignKey(Position,on_delete=models.CASCADE)