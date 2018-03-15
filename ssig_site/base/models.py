from django.db import models
from ssig_site.auth.models import User


# Create your models here.


class Group(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    users = models.ManyToManyField(User, through='GroupUser')

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=200)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    ADMIN = 'a'
    MEMBER = 'r'
    STATUS_CHOICES = (
        (ADMIN, 'Administrator'),
        (MEMBER, 'Member')
    )

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=MEMBER)

    def __str__(self):
        return self.user.upi + ' in ' + self.group.name

    class Meta:
        unique_together = ('user', 'group')
