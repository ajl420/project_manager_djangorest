from app.models import Status
from utils.generic_repo import CrudRepo

class StatusRepo(CrudRepo):
    def __init__(self):
        super().__init__(Status)