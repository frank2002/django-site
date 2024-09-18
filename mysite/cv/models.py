from django.db import models

# Create your models here.


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    localtion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    localtion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.CharField(
        max_length=50
    )  # e.g., Beginner, Intermediate, Advanced

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.CharField(
        max_length=50
    )  # e.g., Beginner, Intermediate, Advanced

    def __str__(self):
        return self.name
