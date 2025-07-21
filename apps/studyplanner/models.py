from django.db import models
from django.conf import settings

class StudyEvent(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='study_events'
    )
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    set_reminder = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.subject})"
