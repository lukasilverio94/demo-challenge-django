from django.urls import path

from . import views

app_name = "items"

urlpatterns = [
    path('', views.items, name="items"),
    path("new/", views.new, name="form"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
]
