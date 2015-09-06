from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^article/(?P<slug>\S+)/$', views.ArticleDetail.as_view(), name='article_ex'),
    url(r'^article/(?P<slug>\S+)$', views.ArticleDetail.as_view(), name='article'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.ArticlesOfCategory, name='category'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.ArticlesOfTag, name='tag'),
    url(r'^$', views.Home, name='home'),
    url(r'^archives/', views.Archives, name='archives'),
    url(r'^works/', views.Works, name='works'),
    url(r'^about/', views.About, name='about'),
    url(r'^book/', views.Book, name='book'),
    url(r'^activity/', views.Activity, name='activity'),
    url(r'^', views.Home, name='home'),
)
