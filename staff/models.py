from django.db import models
from django.contrib.auth.models import User




class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_staff"
        verbose_name = "staff"
        verbose_name_plural = "staffs"
        ordering = ["-id"]


    def __str__(self):
        return self.user.username

