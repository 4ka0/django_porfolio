from django.db import models


'''
model for the database
will contain 5 columns
id, title, description, technology, image
id is an incrementing integer, added automatically by django
'''
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
