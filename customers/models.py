from django.db import models

# Create your models here.
class Customer(models.Model):
  STATUS_CHOICES = [
    ('lead', 'Lead'),
    ('converted', 'Converted'),
    ('lost', 'Lost'),
  ]

  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES)

  def __str__(self):
    return f"{self.name} ({self.status})"