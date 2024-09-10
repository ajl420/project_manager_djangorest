from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.serializers import Serializer

class SimpleSuccessResponse(Response):
    def __init__(self, data: dict, *args, **kwargs):
        super().__init__(
            data=data,
            status=HTTP_200_OK,
            *args,
            **kwargs
        )
class SimpleMessageResponse(SimpleSuccessResponse):
    def __init__(self, message: str, *args, **kwargs):
        super().__init__(
            data={"message": message},
            *args, **kwargs
        )
class SerializerResponse(Response):
    def __init__(self, serializer: Serializer, status: int = HTTP_200_OK , *args, **kwargs):
        super().__init__(
            data= serializer.data,
            status=status,
            *args, **kwargs
        )
class SerializerCreatedResponse(SerializerResponse):
    def __init__(self, serializer: Serializer , *args, **kwargs):
        super().__init__(
            serializer=serializer,
            status=HTTP_201_CREATED,
            *args, **kwargs
        )
