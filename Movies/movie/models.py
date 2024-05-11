from django.db import models

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    duration = models.IntegerField(help_text="Duration in minutes")  # Adjust data type if needed
    userRating = models.FloatField()
    language = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True)  # Optional genre field
    description = models.TextField(blank=True)  # Optional description field

    def __str__(self):
        return self.name  # String representation of the model

    # Optional method for displaying duration in a more user-friendly format
    def get_duration_formatted(self):
        hours, minutes = divmod(self.duration, 60)
        return f"{hours}h {minutes}m" if hours else f"{minutes}m"
