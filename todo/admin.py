from django.contrib import admin
from todo.models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
admin.site.register(Todo,TodoAdmin)