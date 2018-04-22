from django.shortcuts import render, redirect
from django.utils import timezone

from ssig_site.base.models import Group, GroupUser

from . import models


def index(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def group(request, id):
    this_group = Group.objects.all().get(id=id)
    now = timezone.now()
    events = this_group.event_set.filter(end_datetime__gt=now).order_by('start_datetime', 'end_datetime')[:2]
    timespan = 'future'
    if len(events) == 0:
        events = this_group.event_set.filter(end_datetime__lte=now).order_by('-start_datetime', '-end_datetime')[:2]
        timespan = 'past'
    return render(request, 'group-detail.html', {'group': this_group, 'events': events, 'timespan': timespan})


def events(request, filter='all', time='future'):
    groups = Group.objects.all()
    now = timezone.now()

    if filter == 'all':
        events = models.Event.objects.all()
        active_filter = 'All'
    elif filter == 'none':
        events = models.Event.objects.filter(group=None)
        active_filter = 'None'
    else:
        events = models.Event.objects.filter(group=filter)
        active_filter = groups.get(id=filter).name

    if time == 'future':
        events = events.filter(end_datetime__gt=now)
    elif time == 'past':
        events = events.filter(end_datetime__lte=now)

    return render(request, 'events.html', {
        'events': events,
        'groups': groups,
        'filter': filter,
        'active_filter': active_filter,
        'timespan': time,
    })


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

    group_user = GroupUser(group=group, user=current_user)
    group_user.save()
    return redirect('group-detail', id)


def group_leave(request, id):
    group = models.Group.objects.get(id=id)
    current_user = request.user

    GroupUser.objects.get(group=group, user=current_user).delete()
    return redirect('group-detail', id)
