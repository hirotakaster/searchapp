from django.conf.urls import url
from .views import (SearchView)

urlpatterns = [
    url('', SearchView.as_view(), name='index'),
]