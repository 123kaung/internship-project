from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.



class Bid(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bids')
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='freelancer_bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.freelancer.username} - {self.project.title}"