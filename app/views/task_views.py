from rest_framework.viewsets import ViewSet

from app.serializers.task_serializer import TaskCreationSerializer, TaskSerializer
from app.services.task_services import TaskServices
from app.services.services_mediator import TaskServiceCreationMediator, TaskProjectRelationServiceMediator
from utils.exception.data_exception import ObjectDoesNotExist, ValidationErrors, EntityNotRelatedError, \
    AttributeNameError
from utils.rest_response.errors import NotFoundResponse, ValidationErrorsResponse, BadRequestResponse
from utils.rest_response.success import SerializerResponse, SerializerCreatedResponse, SimpleMessageResponse


class TaskViewSet(ViewSet):
    def __init__(self):
        self.task_creation_service = TaskServiceCreationMediator()
        self.task_project_relation_service = TaskProjectRelationServiceMediator()
        self.task_service = TaskServices()
        super().__init__()

    def create(self, request, project_id):
        try:
            serializer = TaskCreationSerializer(data=request.data.dict())
            new_task = self.task_creation_service.create_task(
                project_id,
                serializer=serializer
            )
            return SerializerCreatedResponse(TaskSerializer(new_task))
        except ObjectDoesNotExist as e:
            return NotFoundResponse(e)
        except ValidationErrors as e:
            return ValidationErrorsResponse(e)

    def retrieve(self, request, project_id, task_id):
        try:
            self.task_project_relation_service.check_if_related(project_id, task_id)
            task = self.task_service.find_by_id(pk=task_id)
            serializer = TaskSerializer(task)
            return SerializerResponse(serializer=serializer)
        except ObjectDoesNotExist as e:
            return NotFoundResponse(e)
        except EntityNotRelatedError as e:
            return BadRequestResponse(data={"error": str(e)})

    def delete(self, request, project_id, task_id):
        try:
            self.task_project_relation_service.check_if_related(project_id, task_id)
            self.task_service.delete_by_id(pk=task_id)
            return SimpleMessageResponse(message="Suppression avec success!")
        except ObjectDoesNotExist as e:
            return NotFoundResponse(e)
        except EntityNotRelatedError as e:
            return BadRequestResponse(data={"error": str(e)})

    def list(self, request, project_id):
        try:
            query = request.query_params.dict()
            filter_by = query.get("filter_by")
            filter_value = query.get("filter_value")
            tasks = self.task_project_relation_service.get_tasks_from_project(
                project_id=project_id,
                filter_by=filter_by,
                filter_value=filter_value
            )
            serializer = TaskSerializer(tasks, many=True)
            return SerializerResponse(serializer=serializer)
        except ObjectDoesNotExist as e:
            return NotFoundResponse(e)
        except AttributeNameError as e:
            return BadRequestResponse(data={"error": str(e)})
