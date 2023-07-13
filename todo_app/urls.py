from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("delete/<int:id>", views.delete_todo, name="delete_todo"),
    path("update/<int:id>", views.update_todo, name="update_todo"),
    path("is_completed/<int:id>", views.is_checked, name="is_checked"),
]
