from django.core.validators import RegexValidator
from django.db import models


class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=100)
    name = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " " + str(self.name)


class Worker(models.Model):
    phone_regex = RegexValidator(regex=r'^\+905[0-9]{9}$',
                                 message="Phone number should be in '+905555555555' format")

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=100, null=False)
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " " + str(self.name)


class Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    path = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " " + str(self.name)


class Violation(models.Model):
    id = models.AutoField(primary_key=True)
    cameraId = models.ForeignKey(Camera, on_delete=models.DO_NOTHING, null=False)
    workerId = models.ForeignKey(Worker, on_delete=models.DO_NOTHING, null=True)
    modelId = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=250, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Configuration(models.Model):
    id = models.AutoField(primary_key=True)
    cameraId = models.ForeignKey(Camera, on_delete=models.CASCADE, null=False)
    modelId = models.ForeignKey(Model, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
