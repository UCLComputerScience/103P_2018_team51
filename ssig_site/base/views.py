from django.shortcuts import render
from ssig_site.base.models import Group

from . import models


def index(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def group(request, id):
    this_group = Group.objects.all().get(id=id)
    return render(request, 'group-detail.html', {'group': this_group})


def events(request):
    events = models.Event.objects.all()
    return render(request, 'events.html', { 'events': events })


def event(request, id):
    event = models.Event.objects.get(id=id)
    return render(request, 'event.html', { 'event': event })

