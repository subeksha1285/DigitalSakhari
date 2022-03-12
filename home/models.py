from django.db import models
import os

# create your models here
def get_file_path(request, filename):
    orignal_filename = filename
    return os.path.join("uploads/", filename)

class product(models.Model):
    product_id = models.TextField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=False)
    Description =  models.CharField(max_length=100, null=True, blank=False)

def _str_(self):
    return self.name