from django.urls import path
from . import views
from blog import views as blog_views
# from django.contrib.sitemaps.views import sitemap
# from blog.sitemaps import ArticleSitemap

# sitemaps = {
#     'articles': ArticleSitemap,
# }

urlpatterns = [
    path('submit/', views.submit_article, name='submit_article'),
    path('approve/<int:article_id>/', views.approve_article, name='approve_article'),
    path('success/', views.success, name='success'),
    path('article/<int:article_id>/comment/', views.submit_comment, name='submit_comment'),
    path('article/<int:article_id>/<slug:article_slug>/', views.article_detail, name='article_detail'),
    path('comment/approve/<int:comment_id>/', views.approve_comment, name='approve_comment'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
    path('', blog_views.home, name='home'),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
