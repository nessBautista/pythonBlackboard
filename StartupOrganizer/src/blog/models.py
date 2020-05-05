from datetime import date
from django.db import models
# from django.db.models import (
#     CharField,
#     DateField,
#     ManyToManyField,
#     Model,
#     SlugField,
#     TextField,
#     )
from organizer.models import Startup, Tag


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField()
    # it has a many to many field with Tags and Startups
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)

    class Meta:
        get_latest_by = "pub_date"
        #orders by most recent and by title
        ordering = ["-pub_date", "title"]
        verbose_name = "blog post"

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"