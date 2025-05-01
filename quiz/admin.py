from django.contrib import admin

# Register your models here.
from .models import Contest, Question

admin.site.register(Contest)
admin.site.register(Question)
