from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

#a mode is the single, definitiva source of truth about your data.
#it contains the essential fields and behaviors of the data you're storing.
#Dnago follows the DRY principle. The goal is to define your data model
#in one place and automatically derive things from it.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
        
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    