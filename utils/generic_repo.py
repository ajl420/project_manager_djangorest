from typing import Type
from django.db import models

class GenericRepo:
    queryset = None
    model = None
    def __init__(self, model: Type[models.Model]):
        self.model = model
        self.queryset = model.objects.all()

class SimpleCreateRepo(GenericRepo):
    def __init__(self, model: Type[models.Model]):
        super().__init__(model)
    def create(self, validated_data):
        return self.queryset.create(**validated_data)

class SimpleDeleteRepo(GenericRepo):
    def __init__(self, model: Type[models.Model]):
        super().__init__(model)
    def delete_from_id(self, pk):
        return self.queryset.filter(pk=pk).delete()

class UpdateRepo(GenericRepo):
    def __init__(self, model: Type[models.Model]):
        super().__init__(model)
    def update(self, validated_update_data, pk):
         return self.queryset.filter(pk=pk).update(**validated_update_data)

class FinderRepo(GenericRepo):
    def __init__(self, model: Type[models.Model]):
        super().__init__(model)
    def find_by_id(self, pk):
        return self.queryset.get(pk=pk)