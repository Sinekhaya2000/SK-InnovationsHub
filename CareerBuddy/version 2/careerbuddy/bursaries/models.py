from django.db import models

class Bursary(models.Model):
    name = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    eligibility_criteria = models.TextField()
    application_deadline = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
