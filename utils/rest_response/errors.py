from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from utils.exception.data_exception import ValidationError, ObjectDoesNotExist, ValidationErrors


class BadRequestResponse(Response):
    def __init__(self, data, *args, **kwargs):
        super().__init__(
            data=data,
            status=HTTP_400_BAD_REQUEST,
            *args, **kwargs
        )

class NotFountResponse(Response):
    def __init__(self, exception: ObjectDoesNotExist, *args, **kwargs):
        super().__init__(
            data={"error":str(exception)},
            status=HTTP_404_NOT_FOUND,
            *args, **kwargs
        )

class BadRequestMessageResponse(BadRequestResponse):
    def __init__(self, message: str, data, *args, **kwargs):
        super().__init__(data={"error": message}, *args, **kwargs)
class ValidationErrorResponse(BadRequestMessageResponse):
    def __init__(self, exception: ValidationError, message, *args, **kwargs):
        super().__init__(message= str(exception) , *args, **kwargs)
class ValidationErrorsResponse(BadRequestResponse):
    def __init__(self, error: ValidationErrors, *args, **kwargs):
        super().__init__(data={"errors": error.errors}, *args, **kwargs)