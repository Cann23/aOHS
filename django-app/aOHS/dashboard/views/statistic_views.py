from datetime import datetime, timedelta

from django.db.models import Count
from django.db.models.functions import TruncDay
from django.shortcuts import render, redirect

from django.views import View

from backend.models import Violation, Camera, Model, Worker


class StatisticView(View):
    def get(self, request):
        from_date = datetime.now() - timedelta(days=7)

        violations_last_week = Violation.objects.filter(created__range=[from_date, datetime.now()])\
            .annotate(day=TruncDay('created'))\
            .values('day')\
            .annotate(c=Count('id'))\
            .values('day', 'c')

        # print(violations_last_week)
        return render(request, 'dashboard/listStatistic.html', {'violations': violations_last_week})
