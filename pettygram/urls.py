
"""
Modulo de URLS de pettygram
"""
#modulo de django
from django.urls import path
from django.contrib import admin
# modulo de pettygram
from pettygram  import views as local_views
from posts  import  views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sorted_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    path('posts/',posts_views.list_posts)
    
]
