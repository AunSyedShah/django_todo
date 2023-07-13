from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50, default='', blank=True)
    description = models.TextField(blank=True, default='')
    is_completed = models.BooleanField(default=False)
    todo_image = models.ImageField(upload_to='todo_images/', default=None)

    def __str__(self) -> str:
        return f"{self.id} - {self.title}"