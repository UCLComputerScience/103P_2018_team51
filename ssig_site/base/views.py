from django.shortcuts import render
from ssig_site.base.models import Group


def index(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def group(request, id):
    this_group = Group.objects.all().get(id=id)
    return render(request, 'group-detail.html', {'group': this_group})
