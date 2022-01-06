from django.db import models
from .utils import is_rating, multiple_of_ten


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    release_date = models.DateField()
    # rating = models.PositiveSmallIntegerField()
    rating = models.PositiveSmallIntegerField(validators=[multiple_of_ten])

    us_gross = models.IntegerField(default=0)
    worldwide_gross = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'