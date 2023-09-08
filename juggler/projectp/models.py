from django.db import models

# Create your models here.
class Project(models.Model):
    """Ongoing projects."""
    project_name = models.CharField(max_length=50,help_text="Project name")
    category = models.CharField(max_length=50, help_text="Project category")
    start_date = models.DateField(auto_now_add=True, help_text="Project start date")
    deadline = models.DateField(help_text="Project deadline")

    def __str__(self):
        return self.project_name

class Task(models.Model):
    task_name = models.CharField\
        (max_length=50, help_text="Task")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.BooleanField(default = False, help_text="Task done?")

    def __str__(self):
        return self.task_name