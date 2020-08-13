from django.contrib import admin

from .models import Category
from .models import Answer


admin.site.register(Category)
admin.site.register(Answer)
