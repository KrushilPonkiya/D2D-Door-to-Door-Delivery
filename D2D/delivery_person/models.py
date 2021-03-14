from django.db import models


class Feedback(models.Model):
    feedback_id = models.AutoField
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
