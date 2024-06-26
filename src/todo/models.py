from django.db import models

# Create your models here.


class Todo(models.Model):
    class Meta:
        db_table = 'todo'
        ordering = ['created_at']

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
