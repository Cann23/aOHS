from django.views import generic

from backend.models import Model, Camera


class CameraIndexView(generic.ListView):
    template_name = ''
    context_object_name = 'camera_list'

    def get_queryset(self):
        return Camera.objects.all()



