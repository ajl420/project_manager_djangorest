from app.exceptions.data_exceptions import ProjectDoesNotExist
from app.repositories.project_repo import ProjectRepo
from utils.exception.data_exception import AttributeNameError
from utils.generic_service import MixinCrudService

class ProjectServices(MixinCrudService):
    repo: ProjectRepo
    def __init__(self):
        super().__init__(ProjectRepo(), not_found_exception=ProjectDoesNotExist)
    def get_all(self, order_by=None):
        if order_by is None:
            return super().get_all()
        elif order_by in ["name", "created_at"]:
            return self.repo.get_list_ordered(order_by)
        else:
            raise AttributeNameError(order_by)