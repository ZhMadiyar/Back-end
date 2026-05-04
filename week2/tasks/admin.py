from django.contrib import admin
from .models import Category, Task


# Кастомное действие
@admin.action(description="Отметить выбранные как выполненные")
def make_completed(modeladmin, request, queryset):
    queryset.update(completed=True)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Что отображаем в списке
    list_display = ['id', 'title', 'completed', 'priority', 'category', 'created_at']

    # Фильтры справа
    list_filter = ['completed', 'priority', 'category']

    # Поиск
    search_fields = ['title', 'description']

    # Быстрое редактирование в списке
    list_editable = ['completed', 'priority']

    # Поля только для чтения (их нельзя менять вручную)
    readonly_fields = ['created_at', 'updated_at']

    # Добавляем наше кастомное действие в список действий
    actions = [make_completed]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['id', 'name', 'slug']