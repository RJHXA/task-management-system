from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    task_description = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        db_table = 'Tasks'