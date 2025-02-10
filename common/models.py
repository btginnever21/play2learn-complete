from django.db import models
from django.utils.timezone import now

# Create your models here.
# Contact Form Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"