from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from backend.models import Model
from dashboard.views.mixins import GetCountsMixin


class ModelView(LoginRequiredMixin, View, GetCountsMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        headers = ['id', 'name', 'path']
        models = Model.objects.all()
        return render(request, 'dashboard/listModel.html',
                      {'headers': headers, 'data': models, 'counts': super().get_counts()})

    def put(self, request):
        name = request.PUT['name']
        path = request.PUT['path']
        Model.objects.get(id=request.PUT['id']).update(name=name, path=path)
        return redirect('dashboard/models')

    def delete(self, request):
        Model.objects.get(id=request.DELETE['id']).delete()
        return redirect('dashboard/models')


class ModelEditView(View):
    def get(self, request, model_id):
        model = Model.objects.get(id=model_id)
        return render(request, 'dashboard/model-edit.html', {"model": model})

    def post(self, request, model_id):
        name = request.POST['name']
        path = request.POST['path']
        Model.objects.filter(id=model_id).update(name=name, path=path)
        return redirect('/dashboard/models')


class ModelDeleteView(View):
    def get(self, request, model_id):
        Model.objects.filter(id=model_id).delete()
        return redirect('/dashboard/models')
