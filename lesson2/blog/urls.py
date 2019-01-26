from django.urls import path

from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('about/', views.about, name="about-home")
]
