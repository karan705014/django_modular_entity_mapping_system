from django.db import models
from common.models import TimeStampModel


class Certification(TimeStampModel):

    name = models.CharField(max_length=100)

    code = models.CharField(max_length=50, unique=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
