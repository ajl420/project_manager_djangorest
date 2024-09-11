from app.exceptions.data_exceptions import ProjectDoesNotExist, StatusDoesNotExist, PriorityDoesNotExist
from app.serializers.task_serializer import TaskCreationSerializer
from app.services.priority_services import PriorityServices
from app.services.project_services import ProjectServices
from app.services.status_services import StatusServices
from app.services.task_services import TaskServices
from app.models import Task
from utils.exception.data_exception import ValidationErrors, EntityNotRelatedError

class TaskAndProjectServiceMediator:
    def __init__(self):
        self.task_services = TaskServices()
        self.project_services = ProjectServices()

class TaskServiceCreationMediator(TaskAndProjectServiceMediator):
    def __init__(self):
        super().__init__()
        self.priority_services = PriorityServices()
        self.status_services = StatusServices()

    def create_task(self, project_id, serializer: TaskCreationSerializer):
        serializer.initial_data['project_id'] = project_id
        if serializer.is_valid():
            status_id = serializer.validated_data['status_id']
            priority_id = serializer.validated_data['priority_id']
            try:
                self.check_if_entities_exists(project_id, status_id, priority_id)
                return self.task_services.create(serializer=serializer)
            except ProjectDoesNotExist:
                raise ProjectDoesNotExist()
            except StatusDoesNotExist:
                raise StatusDoesNotExist()
            except PriorityDoesNotExist:
                raise PriorityDoesNotExist()
        else:
            raise ValidationErrors(serializer.errors)

    def check_if_entities_exists(self, project_id, status_id, priority_id):
        self.project_services.find_by_id(pk=project_id)
        self.status_services.find_by_id(pk=status_id)
        self.status_services.find_by_id(pk=priority_id)

class TaskProjectRelationServiceMediator(TaskAndProjectServiceMediator):
    def __init__(self):
        super().__init__()
    def check_if_related(self, project_id, task_id):
        task: Task = self.task_services.find_by_id(task_id)
        if task.project.pk != project_id:
            raise EntityNotRelatedError("projet","tache")
        return True
    def get_tasks_from_project(self, project_id, filter_by, filter_value):
        try:
            self.project_services.find_by_id(pk=project_id)
            return self.task_services.get_all(
                project_id=project_id,
                filter_by=filter_by,
                filter_value=filter_value
            )
        except ProjectDoesNotExist:
            raise ProjectDoesNotExist()
