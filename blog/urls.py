from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_article, name='submit_article'),
    path('approve/<int:article_id>/', views.approve_article, name='approve_article'),
    path('success/', views.success, name='success'),
    path('article/<int:article_id>/comment/', views.submit_comment, name='submit_comment'),
    path('article/<int:article_id>/<slug:article_slug>/', views.article_detail, name='article_detail'),
    path('comment/approve/<int:comment_id>/', views.approve_comment, name='approve_comment'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
]
