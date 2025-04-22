from django.db import models

class Contest(models.Model):
    name = models.CharField(max_length=255)  # Name of the contest
    description = models.TextField(blank=True, null=True)  # Optional description
    start_date = models.DateTimeField()  # Start date and time of the contest
    end_date = models.DateTimeField()  # End date and time of the contest
    is_active = models.BooleanField(default=True)  # Whether the contest is currently active

    def __str__(self):
        return self.name