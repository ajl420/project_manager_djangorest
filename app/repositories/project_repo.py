from app.models import Project
from utils.generic_repo import CrudRepo

class ProjectRepo(CrudRepo):
    def __init__(self):
        super().__init__(Project)
    def get_list_ordered(self, order_by):
        return super().get_all().order_by(order_by)
