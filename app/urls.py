from django.urls import path

from app.views.priority_views import PriorityViewSet
from app.views.status_views import StatusViewSet

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

urlpatterns = [
    path("task-status/", status_list_v, name="status_list"),
    path("task-status/<int:status_id>", status_detail_v, name="status_detail"),
    path(
        "task-priorities-switch-level/",
        priority_switch_v, name="priority_switch"
    ),
    path("task-priorities/", priority_list_v, name="priority_list"),
    path("task-priority/<int:priority_id>", priority_detail_v, name="priority_detail"),


]