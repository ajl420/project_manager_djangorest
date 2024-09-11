from rest_framework import viewsets

from app.exceptions.data_exceptions import StatusDoesNotExist
from app.serializers.task_serializer import StatusSerializer
from app.services.status_services import StatusServices
from utils.exception.data_exception import ValidationErrors
from utils.rest_response.errors import ValidationErrorsResponse, NotFountResponse
from utils.rest_response.success import SimpleSuccessResponse, SerializerResponse, SerializerCreatedResponse, \
    SimpleMessageResponse


class StatusViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        self.status_services = StatusServices()
        super().__init__(**kwargs)

    def list(self, request):
        all_status = self.status_services.get_all()
        return SerializerResponse(StatusSerializer(all_status, many=True))

    def create(self, request):
        try:
            data = request.data.dict()
            new_status = self.status_services.create(
                StatusSerializer(data=data)
            )
            return SerializerCreatedResponse(StatusSerializer(new_status))
        except ValidationErrors as e:
            return ValidationErrorsResponse(e)

    def delete(self, request, status_id):
        try:
            self.status_services.delete_by_id(status_id)
            return SimpleMessageResponse(message="Supprime avec success!")
        except StatusDoesNotExist as e:
            return NotFountResponse(e)

    def update(self, request, status_id):
        try:
            data = request.data.dict()
            self.status_services.update(
                serializer=StatusSerializer(data=data, partial=True),
                pk=status_id
            )
            return SimpleMessageResponse(message="Donnee mis a jour!")
        except ValidationErrors as e:
            return ValidationErrorsResponse(e)
        except StatusDoesNotExist as e:
            return NotFountResponse(e)
