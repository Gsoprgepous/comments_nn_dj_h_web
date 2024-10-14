from django.db import models

class Review(models.Model):
    comment = models.TextField(verbose_name="Comment")
    rating = models.IntegerField(verbose_name="Rating", default=0)  # auto-calculated
    sentiment = models.CharField(max_length=10, verbose_name="Sentiment", default='Unknown')
