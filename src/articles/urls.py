from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<int:article_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.article_create_view, name='create'),
    path('<int:article_id>/delete/', views.article_delete_view, name='delete'),
    path('<int:article_id>/edit/', views.article_edit_view, name='edit'),
    path('<int:article_id>/like/', views.article_like, name='like'),
]