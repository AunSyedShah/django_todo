from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id} - {self.title}"