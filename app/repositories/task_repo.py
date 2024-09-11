from utils.generic_repo import CrudRepo
from app.models import Task

class TaskRepo(CrudRepo):
    def __init__(self):
        super().__init__(Task)

    def get_all(self, project_id=None):
        return super().get_all().filter(project_id=project_id)
    def get_all_filtered_by_status(self,project_id, status_id):
        return self.get_all(project_id).filter(status_id=status_id)
    def get_all_filtered_by_priority(self,project_id, priority_id):
        return self.get_all(project_id).filter(priority_id=priority_id)