from django.db import models


class Message(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        SENT = 'SENT', 'Sent'
        ARCHIVED = 'ARCHIVED', 'Archived'

    text = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.SENT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.text[:50] + '...') if len(self.text) > 50 else self.text