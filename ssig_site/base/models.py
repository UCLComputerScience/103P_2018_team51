from django.db import models
from ssig_site.auth.models import User
from ssig_site.metrics.models import Metric

import qrcode
from qrcode.image.svg import SvgPathImage as qr_image_factory
import xml.etree.ElementTree as ET


class Group(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    users = models.ManyToManyField(User, through='GroupUser')

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    MEMBERS = 'm'
    STUDENTS = 's'
    PUBLIC = ''

    ROLE_CHOICES = (
        (MEMBERS, 'Group Members'),
        (STUDENTS, 'UCL Students and Staff'),
        (PUBLIC, 'Public')
    )

    restricted_to = models.CharField(max_length=2, choices=ROLE_CHOICES, default=STUDENTS, blank=True)

    def __str__(self):
        return self.title

    def get_ticket(self, user):
        try:
            return Ticket.objects.get(event=self, user=user)
        except (Ticket.DoesNotExist, TypeError):
            return None

    def register(self, user):
        ticket = Ticket(event=self, user=user)
        ticket.save()

        Metric(name='event_registration',
               data={'event_id': self.id,
                     'group_id': None if self.group is None else self.group.id,
                     'user_id': user.id,
                     'user_department': user.department,
                     }).save()

        return ticket

    def unregister(self, user):
        try:
            ticket = Ticket.objects.get(event=self, user=user)
            ticket.delete()

            Metric(name='event_registration',
                   increment=-1,
                   data={'event_id': self.id,
                         'group_id': None if self.group is None else self.group.id,
                         'user_id': user.id,
                         'user_department': user.department,
                         }).save()

        except (Ticket.DoesNotExist, TypeError):
            return None

    def attendance(self, user):
        success = False
        ticket = self.get_ticket(user)
        if ticket is None:
            message = f'{user.full_name} has no ticket.'
        elif ticket.attendance:
            message = f'{user.full_name}\'s ticket has already been used.'
        else:
            ticket.attendance = True
            ticket.save()
            success = True
            message = f'Successfully registered {user.full_name}\'s attendance.'

            Metric(name='event_attendance',
                   data={'event_id': self.id,
                         'group_id': None if self.group is None else self.group.id,
                         'user_id': user.id,
                         'user_department': user.department,
                         }).save()

        return {'success': success, 'message': message}


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    attendance = models.BooleanField(default=False)

    class Meta:
        unique_together = ('event', 'user')

    def __str__(self):
        return f"{self.user.upi}'s ticket for {self.event.title}"

    @property
    def qr(self):
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            image_factory=qr_image_factory
        )
        qr.add_data(self.user.upi)

        svg = qr.make_image()
        svg.get_image().append(svg.make_path())
        svg.get_image().set('width', '100%')
        svg.get_image().set('height', 'auto')
        return ET.tostring(svg.get_image(), encoding='unicode')


class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    LEADER = 'l'
    MEMBER = 'm'

    ROLE_CHOICES = (
        (LEADER, 'Leader'),
        (MEMBER, 'Member')
    )

    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=MEMBER)

    def __str__(self):
        return self.user.upi + ' in ' + self.group.name

    class Meta:
        unique_together = ('user', 'group')
