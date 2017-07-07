from django.db import models


class SearchWord(models.Model):
    GOOGLE = 'Google'
    NAVER = 'Naver'
    DAUM = 'Daum'
    NAVER_DICT = 'NDict'

    ENGINE_CHOICES = (
        (GOOGLE, 'Google'),
        (NAVER, 'Naver'),
        (DAUM, 'Daum'),
        (NAVER_DICT, 'Naver_Dict'),
    )

    search_word = models.CharField(max_length=100)
    engine = models.CharField(max_length=10, choices=ENGINE_CHOICES, default=GOOGLE)
    created_at = models.DateTimeField(auto_now_add=True)
