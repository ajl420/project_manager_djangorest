from utils.generic_repo import CrudRepo
from app.models import Task

class TaskRepo(CrudRepo):
    def __init__(self):
        super().__init__(Task)