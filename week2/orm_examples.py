from tasks.models import Task, Category
from django.db.models import Q, Count


all_tasks = Task.objects.all()

category = Category.objects.first()
new_task = Task.objects.create(
    title="ORM задача",
    priority=2,
    category=category
)

completed_tasks = Task.objects.filter(completed=True)

try:
    task_one = Task.objects.get(id=1)
except Task.DoesNotExist:
    task_one = None

Task.objects.filter(id=1).update(title="Обновлено через ORM")



total_count = Task.objects.count()

completed_count = Task.objects.filter(completed=True).count()

priority_distribution = Task.objects.values('priority').annotate(count=Count('id'))


complex_filter_tasks = Task.objects.filter(
    Q(priority=3) | Q(completed=False)
)

django_tasks = Task.objects.filter(
    Q(title__icontains="django") & Q(completed=False)
)



sorted_tasks = Task.objects.order_by('-priority', 'title')