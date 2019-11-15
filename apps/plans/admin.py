from django.contrib import admin
from plans.models import Plan, Todo


class TodoInline(admin.TabularInline):
    model = Todo
    extra = 0


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_filter = ['created_time']
    search_fields = ['plan_title']
    list_display = ('plan_title', 'plan_start_time', 'created_time',
                    'plan_finish_time', 'priority', 'is_finish')
    inlines = [TodoInline]


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_filter = ['created_time']
    search_fields = ['todo_title']
    list_display = ('todo_title', 'created_time', 'is_done', 'plan')
