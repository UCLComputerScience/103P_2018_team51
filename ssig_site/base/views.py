from django.shortcuts import render, redirect

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
    return render(request, 'events.html', {'events': events})


def event(request, id):
    event = models.Event.objects.get(id=id)
    return render(request, 'event.html', {'event': event})


def event_register(request, id):
    event = models.Event.objects.get(id=id)
    current_user = request.user
    current_user.events.add(event)
    return redirect('event', id)


def event_unregister(request, id):
    event = models.Event.objects.get(id=id)
    current_user = request.user

    current_user.events.remove(event)
    return redirect('event', id)


def group_join(request, id):
    group = models.Group.objects.get(id=id)
    current_user = request.user

    current_user.interest_groups.add(group)
    return redirect('group-detail', id)


def group_leave(request, id):
    group = models.Group.objects.get(id=id)
    current_user = request.user

    current_user.interest_groups.remove(group)
    return redirect('group-detail', id)
