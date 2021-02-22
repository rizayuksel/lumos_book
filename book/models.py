from django.db import models

class Bookmark(models.Model):
    username = models.CharField(max_length=100, verbose_name="Username")
    book_code = models.CharField(max_length=25, verbose_name="Book")
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Added Date")

    def __str__(self):
        return "%s" % (self.username)

    class Meta:
        ordering = ['-added_date']
        verbose_name_plural = "Bookmark List"
