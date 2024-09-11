from app.exceptions.data_exceptions import PriorityDoesNotExist
from app.repositories.priority_repo import PriorityRepo
from utils.generic_service import MixinCrudService

class PriorityServices(MixinCrudService):
    def __init__(self):
        super().__init__(PriorityRepo(), not_found_exception=PriorityDoesNotExist())