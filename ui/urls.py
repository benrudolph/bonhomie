from django.conf.urls import patterns, include, url
from .views import BonhomieView

urlpatterns = patterns('',
    url(r'^$', BonhomieView.as_view())
)

