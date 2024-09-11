from rest_framework.serializers import Serializer
from utils.exception.data_exception import ValidationErrors, ObjectDoesNotExist
from utils.generic_repo import GenericRepo, SimpleCreateRepo, FinderRepo, UpdateRepo, SimpleDeleteRepo, CrudRepo, \
    GetAllRepo


class LocalDataService:
    def __init__(
            self,
            repo: GenericRepo,
            not_found_exception: ObjectDoesNotExist = ObjectDoesNotExist(),
            *args, **kwargs
    ):
        self.not_found_exception = not_found_exception
        self.repo = repo
        super().__init__()

class MixinCreateEntityService(LocalDataService):
    repo: SimpleCreateRepo
    def __init__(self, repo: SimpleCreateRepo, *args, **kwargs):
        super().__init__(repo, *args, **kwargs)
    def create(self, serializer: Serializer, *args, **kwargs):
        if serializer.is_valid():
            return self.repo.create(serializer.validated_data)
        else:
            raise ValidationErrors(serializer.errors)

class MixinFinderEntityService(LocalDataService):
    repo: FinderRepo
    def __init__(
            self,
            repo: FinderRepo,
            *args, **kwargs
    ):
        super().__init__(repo, *args, **kwargs)
    def find_by_id(self, pk, *args, **kwargs):
        try:
            return self.repo.find_by_id(pk=pk)
        except self.repo.model.DoesNotExist:
            raise self.not_found_exception

class MixinUpdaterService(LocalDataService):
    repo: UpdateRepo
    def __init__(self, repo: UpdateRepo, *args, **kwargs):
        super().__init__(repo, *args, **kwargs)
    def update(self, serializer: Serializer, pk, *args, **kwargs):
        if serializer.is_valid():
            updated_count =  self.repo.update(serializer.validated_data, pk=pk)
            if updated_count < 1:
                raise self.not_found_exception
        else:
            raise ValidationErrors(serializer.errors)

class MixinDeleterService(LocalDataService):
    repo: SimpleDeleteRepo
    def __init__(self, repo: SimpleDeleteRepo, *args, **kwargs):
        super().__init__(repo, *args, **kwargs)
    def delete_by_id(self, pk, *args, **kwargs):
        deleted_count = self.repo.delete_from_id(pk=pk)[0]
        if deleted_count < 1:
            raise self.not_found_exception

class MixinGetAllService(LocalDataService):
    repo: GetAllRepo
    def __init__(self, repo: GetAllRepo, *args, **kwargs):
        super().__init__(repo, *args, **kwargs)
    def get_all(self):
        return self.repo.get_all()

class MixinCrudService(
    MixinUpdaterService,
    MixinDeleterService,
    MixinFinderEntityService,
    MixinCreateEntityService,
    MixinGetAllService
):
    repo: CrudRepo
    def __init__(self, repo: CrudRepo, *args, **kwargs):
        super().__init__(repo, *args, **kwargs)