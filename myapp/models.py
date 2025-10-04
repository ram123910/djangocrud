from django.db import models

# Create your models here.

# Models  created

# class Teacher(models.Model):
#     Firstname = models.CharField(max_length=50)
#     Lastname = models.CharField(max_length=50)
#     Email =  models.EmailField(max_length=50)
#     Contact = models.CharField(max_length=50)


# This function is used for converting objevct into string
    # def __str__(self):
    #     return self.Firstname

#   new model add krna 

class Student(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email =  models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)


