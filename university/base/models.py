from django.db import models

class Internship(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    stipend = models.CharField(max_length=50)
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
