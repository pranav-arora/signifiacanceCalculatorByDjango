from django.conf.urls import url,include
from .views import significance_view

urlpatterns = [
    url(r'^$',significance_view.as_view(),name='significance_view'),
]