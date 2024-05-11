from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movie, name='movie'),
    path('movielist/', views.movie_list, name="movie_list"),
    path('<int:id>/', views.movie_detail, name='movie_detail'),  
]
