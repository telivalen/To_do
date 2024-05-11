from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
    path("<int:pk>/", TaskDetail.as_view(), name="task_detail"),
]