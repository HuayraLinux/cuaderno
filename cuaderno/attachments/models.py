from django.db import models

from storage import OwnCloudStorage

# Create your models here.

oc = OwnCloudStorage()

class Attachment(models.Model):
    data = models.FileField(storage=oc, upload_to='/huayra-cuaderno')
    created_at = models.DateTimeField(auto_now_add=True)
