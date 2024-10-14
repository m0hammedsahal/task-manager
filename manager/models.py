from django.db import models

from staff.models import *



class Task(models.Model):
    task = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    

    class Meta:
        db_table = 'web_task'
        verbose_name = ('task')
        verbose_name_plural = ('tasks')
        ordering = ['-id']

    def __str__(self):
        return self.task
  