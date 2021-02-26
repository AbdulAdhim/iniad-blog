# auth/urls.py


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from . import views

from post.views import home_feed, blog, post 

urlpatterns = [
    path('', views.home_feed, name='home_feed'),
    path('blog/', views.blog, name='post-list'),
    path('search/', views.search, name='search'),
    path('post/<id>', views.post, name='post-detail'),  
        path('post', views.post, name='post'),  

    # path('chat', views.who_to_chat, name="who_to_chat"),
    path('chat/<str:room_name>/', views.chatroom, name='chatroom'),
    


]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
