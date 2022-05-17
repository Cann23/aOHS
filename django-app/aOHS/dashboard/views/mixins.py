from datetime import datetime, timedelta

from backend.models import Worker, Camera, Violation


class GetCountsMixin(object):
    def get_counts(self):
        violations_in_this_week = Violation.objects.filter(valid=True, created__gte=datetime.now() - timedelta(days=7))
        violations_in_last_week = Violation.objects.filter(valid=True, created__gte=datetime.now() - timedelta(days=14),
                                                           created__lte=datetime.now() - timedelta(7))

        if len(violations_in_last_week) == 0:
            increase = 0
        else:
            increase = len(violations_in_this_week) - len(violations_in_last_week) / len(violations_in_last_week)

        counts = {
            'workers': Worker.objects.filter(active=True).count(),
            'violations': Violation.objects.filter(valid=True).count(),
            'cameras': Camera.objects.count(),
            'increase': increase,
        }

        return counts
