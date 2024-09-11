from app.exceptions.data_exceptions import PriorityDoesNotExist
from app.repositories.priority_repo import PriorityRepo
from utils.generic_service import MixinCrudService

class PriorityServices(MixinCrudService):
    repo: PriorityRepo
    def __init__(self):
        super().__init__(PriorityRepo(), not_found_exception=PriorityDoesNotExist())
    def switch_level(self, first_level: int, second_level: int):
        try:
            first_priority = self.repo.find_by_id(first_level)
            second_priority = self.repo.find_by_id(second_level)
            self.repo.switch_label(first_priority, second_priority)
        except self.repo.model.DoesNotExist:
            raise PriorityDoesNotExist()