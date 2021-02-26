from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from post.models import Post 
from .models import Signup
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json
from django.shortcuts import redirect
from django.db.models import Count, Q



def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')  # getting the q=....
    if query: 
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
        context = {
            'queryset' : queryset
        }
        return render(request, 'auth/search_result.html', context)    



def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset



        





# Create your views here.
def home_feed(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/logout.html', {})

    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email 
        new_signup.save()  # comment to save
    
    
    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'auth/home_feed.html', context)


def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all() 
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'category_count' : category_count

    } 
    return render(request, 'auth/blog.html', context)

def post(request):
    return render(request, 'auth/post.html', {})

@login_required
def chatroom(request, room_name):
    return render(request, 'auth/chatroom.html', {
        'room_name_json' : mark_safe(json.dumps(room_name)),
        'username' : mark_safe(json.dumps(request.user.username)),
    })
