from app.repositories.project_repo import ProjectRepo
from utils.generic_service import MixinCrudService

class ProjectServices(MixinCrudService):
    def __init__(self):
        super().__init__(ProjectRepo())