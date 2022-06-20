from django.db import models

# Create your models here.
JOB_TYPE = (
    ('full time','full time'),
    ('part time','part time'),

)
class job(models.Model):
    title = models.CharField(max_length=100) 
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)

