from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('<int:article_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('create/', views.article_create_view, name='create'),
    path('save/', views.article_save_view, name='save'),
    path('<int:article_id>/delete/', views.article_delete_view, name='delete'),
    path('<int:article_id>/edit/', views.article_edit_view, name='edit'),
    path('<int:article_id>/update/', views.article_update_view, name='update'),
]