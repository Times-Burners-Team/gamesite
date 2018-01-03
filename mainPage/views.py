from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template import RequestContext
from newsPage.models import Articles

def index(request):
    return render(request, 'mainPage/homePage.html')

def news(request):
    posts_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts_list, 8)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    vars = dict(
        posts=posts,
        )
    return render_to_response('news/posts.html', vars, context_instance=RequestContext(request))
