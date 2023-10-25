from django.db import models

class Cars(models.Model):
    make = models.CharField(max_length=30, db_index=True)
    model = models.CharField(max_length=30, db_index=True)
    year = models.IntegerField(blank=True, null=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['make', 'model'], name='unique_attr')]
        ordering = ('make', 'model')

