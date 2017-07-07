from django.conf.urls import url
from search.views import SearchResultAPIView

urlpatterns = [
    url(r'^result/$', SearchResultAPIView.as_view(), name='search_result'),
]
