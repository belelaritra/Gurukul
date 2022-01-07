from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class UploadFiles(models.Model):
    serial_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    ISBN = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=100)
    bookfile = models.FileField(blank=True)
    image_url = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True)

    # Will show the name of the table in the admin page (not Contact_object)
    def __str__(self):
        return str(self.serial_no) + ". " + self.title + " - " + self.author