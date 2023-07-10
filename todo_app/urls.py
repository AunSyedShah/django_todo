from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>', views.delete_todo, name='delete_todo'),
    path('update/<int:id>', views.update_todo, name='update_todo'),
]
