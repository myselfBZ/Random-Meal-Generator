import random 

from django.http import JsonResponse
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic, View
from django.urls import reverse_lazy
from .forms import MealForm
from .models import Meal

class AddYourMeals(generic.CreateView):

    template_name = 'your-meals.html'
    success_url = 'your-meals'
    form_class = MealForm
    model = Meal
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        meals = request.user.meal_set.all()
        response = super().get(request, *args, **kwargs)
        context = {'meals':meals}
        response.context_data.update(context)
        
        return response
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response

class RandomMeal(generic.DetailView):
    
    model = Meal
    template_name = 'sucker.html'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
         meals = Meal.objects.filter(user=self.request.user)
         randomMeal = random.choice(meals)
         return randomMeal
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        context['meal'] = self.get_object()
        

        return context

class DeleteMeal(generic.DeleteView):
    
    model = Meal
    success_url = reverse_lazy('your-meals')
