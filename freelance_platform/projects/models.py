from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Project(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    posted_on = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title