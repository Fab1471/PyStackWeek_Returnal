from django.db import models

# Create your models here.

class Links(models.Model):
    redirect_link = models.URLField()
    token = models.CharField(max_length=12, unique=True, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DurationField(null=True, blank=True)
    max_uniques_cliques = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
