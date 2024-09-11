from rest_framework.viewsets import ViewSet

from app.exceptions.data_exceptions import ProjectDoesNotExist
from app.serializers.project_serializer import ProjectSerializer
from app.services.project_services import ProjectServices
from utils.exception.data_exception import ValidationErrors, AttributeNameError
from utils.rest_response.errors import ValidationErrorsResponse, NotFoundResponse, BadRequestResponse
from utils.rest_response.success import SerializerCreatedResponse, SimpleMessageResponse, SerializerResponse


class ProjectViewSet(ViewSet):
    def __init__(self):
        self.project_services = ProjectServices()
        super().__init__()

    def create(self, request):
        try:
            data = request.data.dict()
            new_project = self.project_services.create(
                ProjectSerializer(data=data)
            )
            return SerializerCreatedResponse(ProjectSerializer(new_project))
        except ValidationErrors as e:
            return ValidationErrorsResponse(e)

    def list(self, request):
        try:
            query = request.query_params.dict()
            order_by = query.get("order_by")
            projects = self.project_services.get_all(order_by=order_by)
            return SerializerResponse(ProjectSerializer(projects, many=True))
        except AttributeNameError as e:
            return BadRequestResponse(data={"error": str(e)})

    def delete(self, request, project_id):
        try:
            self.project_services.delete_by_id(project_id)
            return SimpleMessageResponse(message="Supprime avec success!")
        except ProjectDoesNotExist as e:
            return NotFoundResponse(e)

    def update(self, request, project_id):
        try:
            data = request.data.dict()
            self.project_services.update(
                serializer=ProjectSerializer(data=data, partial=True),
                pk=project_id
            )
            return SimpleMessageResponse(message="Donnee mis a jour!")
        except ValidationErrors as e:
            return ValidationErrorsResponse(e)
        except ProjectDoesNotExist as e:
            return NotFoundResponse(e)