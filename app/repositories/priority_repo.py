from app.models import Priority
from utils.generic_repo import CrudRepo

class PriorityRepo(CrudRepo):
    def __init__(self):
        super().__init__(Priority)