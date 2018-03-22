from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models.functions import Trunc
from django.db.models import Sum, Func

from . import models
from ssig_site.auth.decorators import staff_only


def fetch_data(period, filter):
    valid_periods = ('cumulative', 'month', 'week', 'day')
    if period in valid_periods:
        if period == 'cumulative':
            metrics = list(
                models.Metric.objects
                .filter(**filter)
                .annotate(total=Func(
                    Sum('increment'),
                    template='%(expressions)s OVER (ORDER BY %(order_by)s)',
                    order_by='datetime'
                ))
                # Reference: https://stackoverflow.com/a/43520109
                .annotate(date=Trunc('datetime', 'second'))
                .values('date', 'total')
            )
        else:
            metrics = list(
                models.Metric.objects
                .filter(**filter)
                .annotate(date=Trunc('datetime', period))
                .values('date')
                .annotate(total=Sum('increment'))
                .values('date', 'total')
            )
        return JsonResponse(metrics, safe=False)
    else:
        return HttpResponse(status=404)


@staff_only
def index(request):
    return render(request, 'metrics.html')


@staff_only
def data(request, name, period):
    return fetch_data(period, {'name': name})
