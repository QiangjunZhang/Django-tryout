from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('<int:article_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
    path('create/', views.article_create_view, name='create'),
    path('save/', views.article_save_view, name='save'),
    path('<int:article_id>/delete/', views.article_delete_view, name='delete'),
]