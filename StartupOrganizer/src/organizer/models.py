from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = AutoSlugField(
        help_text="A label for URL Config", max_length=31, populate_from=["name"],
    )

    class Meta:
        # orders alphabetically by name
        ordering = ["name"]

    def __str__(self):
        return self.name


class Startup(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text="A label for Config.")
    description = models.TextField()
    founded_date = models.DateField("Date Founded")
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    # it has a many to many field with Tags
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        # gets the latest sorted by founded date
        get_latest_by = "founded_date"

        # orders alphabetically by name
        ordering = ["name"]


class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    pub_date = models.DateField("Date Published")
    link = models.URLField(max_length=255)
    # One to many collection with a startup
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)

    class Meta:
        # gets the latest sorted by founded date
        get_latest_by = "pub_date"
        # minus sign indicates ordering in descending order
        ordering = ["-pub_date"]
        # Sets of field names that, taken together, must be unique.
        # This is specified by tuple(s)
        unique_together = ("slug", "startup")

        verbose_name = "news article"

    def __str__(self):
        return f"{self.startup}:{self.title}"
