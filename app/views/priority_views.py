from rest_framework import viewsets

from app.exceptions.data_exceptions import PriorityDoesNotExist
from app.serializers.task_serializer import PrioritySerializer
from app.services.priority_services import PriorityServices
from utils.exception.data_exception import ValidationErrors
from utils.rest_response.errors import ValidationErrorsResponse, NotFountResponse
from utils.rest_response.success import SerializerResponse, SerializerCreatedResponse, SimpleMessageResponse


class PriorityViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        self.priority_services = PriorityServices()
        super().__init__(**kwargs)

    def list(self, request):
        all_priorities = self.priority_services.get_all()
        return SerializerResponse(PrioritySerializer(all_priorities, many=True))

    def create(self, request):
        try:
            data = request.data.dict()
            new_status = self.priority_services.create(
                PrioritySerializer(data=data)
            )
            return SerializerCreatedResponse(PrioritySerializer(new_status))
        except ValidationErrors as e:
            return ValidationErrorsResponse(e)

    def delete(self, request, priority_id):
        try:
            self.priority_services.delete_by_id(priority_id)
            return SimpleMessageResponse(message="Supprime avec success!")
        except PriorityDoesNotExist as e:
            return NotFountResponse(e)

    def update(self, request, priority_id):
        try:
            data = request.data.dict()
            self.priority_services.update(
                serializer=PrioritySerializer(data=data, partial=True),
                pk=priority_id
            )
            return SimpleMessageResponse(message="Donnee mis a jour!")
        except ValidationErrors as e:
            return ValidationErrorsResponse(e)
        except PriorityDoesNotExist as e:
            return NotFountResponse(e)

    def switch_level(self, request):
        try:
            data = request.data.dict()
            first_priority_level = data.get("first_priority_level")
            second_priority_level = data.get("second_priority_level")
            self.priority_services.switch_level(first_priority_level, second_priority_level)
            return SimpleMessageResponse(message="Donnee mis a jour!")
        except PriorityDoesNotExist as e:
            return NotFountResponse(e)


