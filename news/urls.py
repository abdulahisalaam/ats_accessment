from django.urls import path


from . import views

app_name = 'news'

urlpatterns = [
    path("", views.NewsListView.as_view(), name="home"),
    path("create/news", views.NewsCreateView.as_view(), name="create-news"),
    path("news/<pk>/details", views.NewsDetailView.as_view(), name="news-details"),
]


