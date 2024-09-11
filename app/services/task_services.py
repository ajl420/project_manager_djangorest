from app.exceptions.data_exceptions import TaskDoesNotExist
from app.repositories.task_repo import TaskRepo
from utils.generic_service import MixinCrudService

class TaskServices(MixinCrudService):
    def __init__(self):
        super().__init__(TaskRepo(), not_found_exception=TaskDoesNotExist)
