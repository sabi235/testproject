from django.contrib.gis.db import models


class Blog(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super(Blog, self).__init__(*args, **kwargs)
        self.author = self.author
        self.title = self.title
        self.text = self.text
        self.created_date = self.created_date
        self.published_date = self.published_date

    def save(self, *args, **kwargs):
        return super(Blog, self).save(*args, **kwargs)