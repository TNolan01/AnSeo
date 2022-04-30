from django.db import models
from django.urls import reverse

class Player(models.Model):
    name = models.CharField(max_length=100, null=False)
    date_of_birth = models.DateField(null=True)
    contact = models.CharField(max_length=200, null=True)
    irish_name = models.CharField(max_length=200, null=True, default='to be confirmed')
        
    def __str__(self):
        return self.name
    
    
class Training(models.Model):
    session_name = models.CharField(max_length=200, null=True)
    session_date = models.DateField()
        
    def __str__(self):
        return str(self.session_date)

class Training(models.Model):
    CHOICES= (
        ('Absent', 'Absent'),
        ('Present', 'Present'),
    )
    player = models.ManyToManyField('Player')
    training = models.ForeignKey(Session, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=CHOICES)