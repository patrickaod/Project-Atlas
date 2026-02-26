from django.db import models

class JournalEntry(models.Model):
    task_name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    energy_level = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 scale
    focus_level = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 scale
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_name} - {self.created_at}"