class MultiException(Exception):
    def __init__(self, errors: dict):
        self.errors = errors
        super().__init__(str(errors))

class ObjectDoesNotExist(Exception):
    def __init__(self, obj_name="Object"):
        super().__init__(f"Ce/Cette {obj_name} n'existe pas")

class ValidationError(Exception):
    def __init__(self, message="Le donnee entree est invalide"):
        super().__init__(message)

class ValidationErrors(MultiException):
    def __init__(self, errors: dict):
        super().__init__(errors)

class AttributeNameError(Exception):
    def __init__(self, attribute: str):
        super().__init__(f"L'attribut {attribute} n'existe pas")

class EntityNotRelatedError(Exception):
    def __init__(self, obj_name_1, obj_name_2):
        super().__init__(f"Ce/cette {obj_name_1} n'appartient pas a ce/cette {obj_name_2}")