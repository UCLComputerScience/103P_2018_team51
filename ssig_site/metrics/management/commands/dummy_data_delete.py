from django.core.management.base import BaseCommand
from ssig_site.metrics.models import Metric


class Command(BaseCommand):
    def handle(self, *args, **options):
        Metric.objects.filter(data__dummy=True).delete()
