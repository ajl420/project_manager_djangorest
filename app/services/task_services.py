from app.repositories.task_repo import TaskRepo
from utils.generic_service import MixinCrudService

class TaskServices(MixinCrudService):
    def __init__(self):
        super().__init__(TaskRepo())
