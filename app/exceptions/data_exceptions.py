from utils.exception.data_exception import ObjectDoesNotExist

class StatusDoesNotExist(ObjectDoesNotExist):
    def __init__(self):
        super().__init__(obj_name="status")

class PriorityDoesNotExist(ObjectDoesNotExist):
    def __init__(self):
        super().__init__(obj_name="priorite")

class ProjectDoesNotExist(ObjectDoesNotExist):
    def __init__(self):
        super().__init__(obj_name="projet")

class TaskDoesNotExist(ObjectDoesNotExist):
    def __init__(self):
        super().__init__(obj_name="tache")