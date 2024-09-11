from django.urls import path
from app.views.status_views import StatusViewSet

status_list_v = StatusViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

status_detail_v = StatusViewSet.as_view({
    'delete': 'delete',
    'put': 'update',
})

urlpatterns = [
    path("task-status/", status_list_v, name="status_list"),
    path("task-status/<int:status_id>", status_detail_v, name="status_detail"),
]