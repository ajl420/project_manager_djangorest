from app.exceptions.data_exceptions import TaskDoesNotExist
from app.repositories.task_repo import TaskRepo
from utils.exception.data_exception import AttributeNameError
from utils.generic_service import MixinCrudService

class TaskServices(MixinCrudService):
    repo: TaskRepo
    def __init__(self):
        super().__init__(TaskRepo(), not_found_exception=TaskDoesNotExist)
    def get_all(self, filter_by:str = None, filter_value:str = None,project_id=None):
        if filter_by is None or filter_value is None:
            return self.repo.get_all(project_id)
        if filter_by  == "status" and filter_value is not None:
            return self.repo.get_all_filtered_by_status(project_id, filter_value)
        if filter_by == "priority" and filter_value is not None:
            return self.repo.get_all_filtered_by_priority(project_id, filter_value)
        if filter_by not in ["status", "priority"]:
            raise AttributeNameError(filter_by)



