from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    
    def __str__(self):
        return self.title