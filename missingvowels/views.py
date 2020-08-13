from django.views import generic

from .models import Category


class CategoryIndexView(generic.ListView):
    template_name = "missingvowels/category/index.html"
    context_object_name = "recent_categories"

    def get_queryset(self):
        return Category.objects.order_by("-id")[:5]
