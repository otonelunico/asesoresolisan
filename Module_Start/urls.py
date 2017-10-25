from django.conf.urls import url, include
from .views import Index, Admin

urlpatterns = [
    url(r'^$', (Index.as_view()),name='home'),
    url(r'^edit/$', (Admin.as_view()),name='edit'),
    ]