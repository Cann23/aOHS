from django.contrib import admin

# Register your models here.
from .models import Worker, Camera, Configuration, Model, Violation, Profile

admin.site.register(Worker)
admin.site.register(Camera)
admin.site.register(Configuration)
admin.site.register(Model)
admin.site.register(Violation)
admin.site.register(Profile)
