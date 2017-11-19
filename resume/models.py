from django.db import models

# Create your models here.
class Name(models.Model):
    first_name=models.CharField(max_length=200)
    middle_name=models.CharField(max_length=200,blank=True)
    last_name=models.CharField(max_length=200,blank=True)

class Experience(models.Model):
    institution_name=models.CharField(max_length=200)
    start_date=models.DateField
    end_date=models.DateField(blank=True)
    present=models.BooleanField
    description=models.TextField(blank=True)

class School(models.Model):
    institution_name=models.CharField(max_length=200)
    class_div=models.CharField(max_length=200)
    start_date=models.DateField
    end_date=models.DateField
    score=models.CharField(max_length=200)

class College(models.Model):
    institution_name = models.CharField(max_length=200)
    degree=models.CharField(max_length=200)
    programme=models.CharField(max_length=200)
    start_date = models.DateField
    end_date = models.DateField
    score = models.CharField(max_length=200)

class Skills(models.Model):
    skill_name=models.CharField(max_length=200)


class Projects(models.Model):
    institution_name = models.CharField(max_length=200,blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    present = models.BooleanField(blank=True)
    description = models.TextField

class Achievements(models.Model):
    details=models.TextField(blank=True)

class Certifications(models.Model):
    name=models.CharField(max_length=200)
    institution_name = models.CharField(max_length=200, blank=True)
    end_date = models.DateField(blank=True)

