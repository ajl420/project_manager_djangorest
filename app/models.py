from django.db import models

class Status(models.Model):
    label = models.CharField(max_length=100, null=False)

class Priority(models.Model):
    label = models.CharField(max_length=100, null=False)
    level = models.IntegerField(null=False)

class Project(models.Model):
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.TextField()