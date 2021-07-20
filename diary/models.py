from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="diary/", blank=True, null=True)
    body = models.TextField()
    pub_date = models.DateField()
    weather = models.CharField(max_length=30)

def __str__(self):
    return self.title