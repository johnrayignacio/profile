from django.db import models

class Works(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(null=True)
    link = models.URLField(max_length=500, null=True)
    label_choices = (
        ('Web Development', 'Web Development'),
        ('Data Science', 'Data Science')
    )
    label = models.CharField(max_length=50, null=True, choices=label_choices)

    def __str__(self):
        return self.title

# Create your models here.
