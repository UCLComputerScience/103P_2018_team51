from django.shortcuts import render, redirect

from ssig_site.base.models import Group, GroupUser

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

    group_user = GroupUser(group=group, user=current_user)
    group_user.save()
    return redirect('group-detail', id)


def group_leave(request, id):
    group = models.Group.objects.get(id=id)
    current_user = request.user

    GroupUser.objects.get(group=group, user=current_user).delete()
    return redirect('group-detail', id)
