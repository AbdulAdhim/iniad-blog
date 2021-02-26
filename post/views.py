from django.shortcuts import render
from .models import Post

# Create your views here.
def home_feed(request):
    queryset = Post.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'auth/home_feed.html', context)


def blog(request):
    return render(request, 'auth/blog.html', {})

def post(request):
    return render(request, 'auth/post.html', {})



