from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.shortcuts import render
from django.views import View

from backend.models import Violation
from dashboard.views.mixins import GetCountsMixin


class StatisticView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        from_date_weekly = datetime.now() - timedelta(days=7)
        from_date_monthly = datetime.now() - timedelta(days=30)

        violations_last_week = Violation.objects.filter(created__range=[from_date_weekly, datetime.now()]) \
            .exclude(workerId__isnull=True) \
            .annotate(day=TruncDay('created')) \
            .values('day') \
            .annotate(c=Count('id')) \
            .values('day', 'c')

        for v in violations_last_week:
            v['day'] = v['day'].date()

        violations_last_month = Violation.objects.filter(created__range=[from_date_monthly, datetime.now()]) \
            .exclude(workerId__isnull=True) \
            .annotate(day=TruncDay('created')) \
            .values('day') \
            .annotate(c=Count('id')) \
            .values('day', 'c')

        for v in violations_last_month:
            v['day'] = v['day'].date()

        violation_by_worker = Violation.objects \
            .values('workerId') \
            .annotate(c=Count('id')) \
            .order_by()

        violation_by_camera = Violation.objects \
            .values('cameraId') \
            .annotate(c=Count('id')) \
            .order_by()

        violation_by_model = Violation.objects \
            .values('modelId') \
            .annotate(c=Count('id')) \
            .order_by()

        return render(request, 'dashboard/listStatistic.html',
                      {'violations_weekly': violations_last_week, "violations_monthly": violations_last_month,
                       'violation_by_worker': violation_by_worker, "violation_by_camera": violation_by_camera,
                       "violation_by_model": violation_by_model, 'counts': super().get_counts()})
