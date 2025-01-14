from django.urls import path

from app.views.priority_views import PriorityViewSet
from app.views.project_views import ProjectViewSet
from app.views.status_views import StatusViewSet
from app.views.task_views import TaskViewSet

status_list_v = StatusViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

status_detail_v = StatusViewSet.as_view({
    'delete': 'delete',
    'put': 'update',
})

priority_list_v = PriorityViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

priority_detail_v = PriorityViewSet.as_view({
    'delete': 'delete',
    'put': 'update',
})

priority_switch_v = PriorityViewSet.as_view({
    'put': 'switch_level',
})

project_list_v = ProjectViewSet.as_view({
    'post': 'create',
    'get': 'list',
})

project_detail_v = ProjectViewSet.as_view({
    'delete': 'delete',
    'put': 'update',
})

task_list_v = TaskViewSet.as_view({
    'post': 'create',
    'get': 'list',
})

task_detail_v = TaskViewSet.as_view({
    'get': 'retrieve',
    'delete': 'delete',
})

urlpatterns = [
    path("task-status/", status_list_v, name="status_list"),
    path("task-status/<int:status_id>", status_detail_v, name="status_detail"),
    path("task-priorities-switch-level/",priority_switch_v, name="priority_switch"),
    path("task-priorities/", priority_list_v, name="priority_list"),
    path("task-priority/<int:priority_id>", priority_detail_v, name="priority_detail"),
    path("projects/", project_list_v, name="project_list"),
    path("project/<int:project_id>", project_detail_v, name="project_detail"),
    path("project/<int:project_id>/tasks/", task_list_v, name="task_list"),
    path("project/<int:project_id>/task/<int:task_id>", task_detail_v, name="task_detail"),
]