from django.db import models

class Contest(models.Model):
    name = models.CharField(max_length=255)  # Name of the contest
    description = models.TextField(blank=True, null=True)  # Optional description
    start_date = models.DateTimeField()  # Start date and time of the contest
    end_date = models.DateTimeField()  # End date and time of the contest
    is_active = models.BooleanField(default=True)  # Whether the contest is currently active
    category = models.CharField(max_length=100)  # Category of the contest
    duration = models.IntegerField(help_text="Duration in minutes")  # Duration of the contest in minutes
    number_of_participants = models.PositiveIntegerField(default=0)  # Number of participants
    image = models.ImageField(upload_to='contest_images/', blank=True, null=True)  # Image for the contest

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()  # The question text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the question was created
    contest = models.ForeignKey('Contest', on_delete=models.CASCADE, related_name='questions')  # Link to a contest

    def __str__(self):
        return self.text[:50]  # Return the first 50 characters of the question