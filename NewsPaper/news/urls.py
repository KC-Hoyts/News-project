from django.urls import path
from .views import NewsList, OneNews, NewsSearch, PostCreate, PostArCreate, PostUpdate, PostDelete


urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>', OneNews.as_view(), name='post_view'),
    path('search/', NewsSearch.as_view(), name='post_search'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('article/create/', PostArCreate.as_view(), name='art_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),


]