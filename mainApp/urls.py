from django.urls import path
from . import views
urlpatterns = [
    path('your-meals', views.AddYourMeals.as_view(), name='your-meals'),
    path('random-meal', views.RandomMeal.as_view(), name='random-meal'),
    path('delete/<int:pk>', views.DeleteMeal.as_view(), name='delete-meal')
]