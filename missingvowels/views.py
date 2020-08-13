from django.views import generic

from .models import Category


class CategoryIndexView(generic.ListView):
    template_name = "missingvowels/category/index.html"
    context_object_name = "recent_categories"

    def get_queryset(self):
        return Category.objects.order_by("-id")[:5]


class CategoryDetailView(generic.DetailView):
    template_name = "missingvowels/category/detail.html"
    model = Category
    context_object_name = "category"
