from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, subscribe
from django.contrib import admin
from django.urls import include
from .views import IndexView
from .views import CategoryListView
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60*1)(PostList.as_view()), name='post_list'),
    path('search/', PostList.as_view()),
    path('<int:pk>/', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('profile/', IndexView.as_view()),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name= 'subscribe'),


]


