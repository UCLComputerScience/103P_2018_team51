from django.db import models  # noqa

# Create your models here.


class Group(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name
