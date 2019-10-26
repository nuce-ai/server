from django.db import models

# Create your models here.
class Image(models.Model):
    iid = models.CharField(max_length=255)
    content = models.TextField()
    label  = models.TextField()
    def __str__(self):
        return self.iid
