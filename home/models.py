from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    isbn = models.CharField(max_length=13, blank=False)
    author = models.CharField(max_length=255, blank=False)
    topic = models.ForeignKey(Topic, default=1, related_name="books", on_delete=models.PROTECT)
    
    def __str__(self):
        return "{0} by {1}".format(self.title, self.author)