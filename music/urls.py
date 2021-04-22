from django.urls import path

from music import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('author', views.author, name = 'author'),
    path('list', views.list_musics, name = 'music_detail_list'),
    path('new/', views.create_music, name='add_music'),
    path('update/<int:id>/', views.update_music, name='update_music'),
    path('delete/<int:id>/', views.delete_music, name='delete_music'),
    path('search/', views.search, name = 'search'),
]
