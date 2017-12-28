
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from newsPage.models import Articles
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name = "news/post.html")),
    url(r'^$', views.index, name='index'),
]
