from app.repositories.status_repo import StatusRepo
from utils.generic_service import MixinCrudService

class StatusServices(MixinCrudService):
    def __init__(self):
        super().__init__(StatusRepo())