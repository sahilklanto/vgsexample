from django.db import models


class VGSRequest(models.Model):
    response = models.TextField()

    def __str__(self):
        return f"{self.id}"
