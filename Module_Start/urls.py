from django.conf.urls import url, include
from .views import Index, Admin
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', (Index.as_view()),name='home'),
    url(r'^edit/$', login_required(Admin.as_view()),name='edit'),
    ]