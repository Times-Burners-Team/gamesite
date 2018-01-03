
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from newsPage.models import Articles

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
]
