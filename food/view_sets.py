from rest_framework import viewsets
from django.db.models import Count, Prefetch
from food.models import FoodCategory, Food
from food.serializers import FoodListSerializer


class FoodListViewSet(viewsets.ModelViewSet):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.prefetch_related(Prefetch(
            'food',
            queryset=Food.objects.filter(is_publish=True))
        ).annotate(number_of_food=Count('food')).filter(number_of_food__gt=0).order_by("id")
        return queryset
