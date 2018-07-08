import uuid
from datetime import datetime
from django.db import models


# Create your models here.
# pass adminpassword

class Question(models.Model):
    LANGUAGES = (
        ('1', 'C++'),
        ('2', 'Python'),
        ('3', 'Django'),
        ('4', 'Java'),
        ('5', 'Shell'),
        ('6', 'C'),
        ('7', 'Panda'),
        ('8', 'TensorFlow')
    )

    id = models.CharField(unique=True, default=uuid.uuid4, editable=False, max_length=50, primary_key=True)
    que = models.TextField(null=True)
    author = models.CharField(max_length=100)
    date_que = models.DateTimeField(blank=True, auto_now=True)
    category = models.CharField(max_length=100, choices=LANGUAGES)

    class Meta:
        ordering = ('date_que',)
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.get_category_display() + " - " + self.que

    def category_print(self):
        return self.get_category_display()


class Answer(models.Model):
    id = models.CharField(unique=True, default=uuid.uuid4, editable=False, max_length=50, primary_key=True)
    que_id = models.CharField(blank=True, null=True, max_length=50)
    answer = models.TextField(null=True)
    author = models.CharField(max_length=100)
