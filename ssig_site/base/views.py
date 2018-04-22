from django.shortcuts import render, redirect
from django.utils import timezone

from . import models, forms


def group_user_role(group, user):
    try:
        group_user = models.GroupUser.objects.get(user=user, group=group)
        return group_user.role
    except (models.GroupUser.DoesNotExist, TypeError):
        return None


def allow_registration(event, user):
    return (
        (event.restricted_to != event.PUBLIC and user.is_staff) or
        (event.restricted_to == event.STUDENTS and user.is_authenticated) or
        (event.restricted_to == event.MEMBERS and group_user_role(event.group, user))
    )


def index(request):
    groups = models.Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def group(request, id):
    this_group = models.Group.objects.all().get(id=id)
    now = timezone.now()
    events = this_group.event_set.filter(end_datetime__gt=now).order_by('start_datetime', 'end_datetime')[:2]
    timespan = 'future'
    if len(events) == 0:
        events = this_group.event_set.filter(end_datetime__lte=now).order_by('-start_datetime', '-end_datetime')[:2]
        timespan = 'past'

    return render(request, 'group-detail.html', {
        'group': this_group,
        'events': events,
        'timespan': timespan,
        'user_role': group_user_role(this_group, request.user),
        'leader_role': models.GroupUser.LEADER,
    })


def events(request, filter='all', time='future'):
    groups = models.Group.objects.all()
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
    return render(request, 'event.html', {'event': event,
                                          'user_role': group_user_role(event.group, request.user),
                                          'leader_role': models.GroupUser.LEADER,
                                          'allow_registration': allow_registration(event, request.user)})


def event_register(request, id):
    event = models.Event.objects.get(id=id)
    if allow_registration(event, request.user):
        request.user.events.add(event)
    return redirect('event', id)


def event_unregister(request, id):
    event = models.Event.objects.get(id=id)
    current_user = request.user

    current_user.events.remove(event)
    return redirect('event', id)


def event_edit(request, id):
    event = models.Event.objects.get(id=id)
    if request.user.is_staff or group_user_role(event.group, request.user) == models.GroupUser.LEADER:

        if request.method == 'GET':
            form = forms.EventForm(instance=event)
            return render(request, 'create-event.html', {'group': event.group, 'form': form})

        if request.method == 'POST':
            form = forms.EventForm(request.POST)
            if form.is_valid():
                models.Event.objects.filter(id=id).update(**form.cleaned_data)
                return redirect('event', event.id)
            else:
                return render(request, 'create-event.html', {'group': group, 'form': form})


def event_delete(request, id):
    event = models.Event.objects.get(id=id)
    if request.user.is_staff or group_user_role(event.group, request.user) == models.GroupUser.LEADER:
        event = models.Event.objects.get(id=id)
        event.delete()
        return redirect('events')


def group_join(request, id):
    group = models.Group.objects.get(id=id)
    current_user = request.user

    group_user = models.GroupUser(group=group, user=current_user)
    group_user.save()
    return redirect('group-detail', id)


def group_leave(request, id):
    group = models.Group.objects.get(id=id)
    current_user = request.user

    models.GroupUser.objects.get(group=group, user=current_user).delete()
    return redirect('group-detail', id)


def create_event(request, id):
    group = models.Group.objects.get(id=id)
    if request.user.is_staff or group_user_role(group, request.user) == models.GroupUser.LEADER:

        if request.method == 'GET':
            form = forms.EventForm(initial={'group': group})
            return render(request, 'create-event.html', {'group': group, 'form': form})

        if request.method == 'POST':
            form = forms.EventForm(request.POST)
            if form.is_valid():
                event = models.Event(**form.cleaned_data)
                event.save()
                return redirect('event', event.id)
            else:
                return render(request, 'create-event.html', {'group': group, 'form': form})
