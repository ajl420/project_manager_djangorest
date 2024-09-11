from app.models import Project
from utils.generic_repo import CrudRepo

class ProjectRepo(CrudRepo):
    def __init__(self):
        super().__init__(Project)