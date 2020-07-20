from django.contrib import admin

# Register your models here.
from .models import TodoModel
# Register your models here.


admin.site.register(TodoModel)