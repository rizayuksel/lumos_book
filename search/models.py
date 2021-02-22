from django.db import models

#Elasticsearch, pulls data from this model.

class SearchTable(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    author = models.CharField(max_length=150, verbose_name="Author")
    isbn13 = models.CharField(max_length=40, verbose_name="Isbn13")
    image = models.CharField(max_length=50, verbose_name="Image")
    keyword = models.CharField(max_length=350, verbose_name="Keywords")

    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        verbose_name_plural = "Search Table"