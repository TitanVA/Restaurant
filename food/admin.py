from django.contrib import admin

from food.models import FoodCategory, Food

admin.site.register(FoodCategory)
admin.site.register(Food)
