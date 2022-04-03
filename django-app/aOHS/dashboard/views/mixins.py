from backend.models import Worker, Camera, Violation


class GetCountsMixin(object):
    def get_counts(self):
        counts = {
            'workers': Worker.objects.filter(active=True).count(),
            'violations': Violation.objects.filter(valid=True).count(),
            'cameras': Camera.objects.count(),
        }

        return counts
