from django.db import models


class SearchWord(models.Model):
    search_word = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
