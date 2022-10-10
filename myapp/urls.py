from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("my-view/", Myview.as_view()),
    path("protect/", ProtectedView.as_view()),
    path("list/", PublisherListView.as_view()),
    path("<int:pk>/delete/", PublisherDeleteView.as_view()),
    path("<int:id>/detail/", PublisherDetailView.as_view()),
    path("create/", PublisherCreateView.as_view()),
    path("<int:pk>/update/", PublisherUpdateView.as_view())
    ]
