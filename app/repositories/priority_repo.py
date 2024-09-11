from app.models import Priority
from utils.generic_repo import CrudRepo

class PriorityRepo(CrudRepo):
    def __init__(self):
        super().__init__(Priority)

    @staticmethod
    def switch_label(first_priority, second_priority):
        tmp_label = first_priority.label
        first_priority.label = second_priority.label
        second_priority.label = tmp_label
        first_priority.save()
        second_priority.save()
