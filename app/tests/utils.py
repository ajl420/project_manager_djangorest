from app.models import Status, Priority, Project


class StatusDBFiller:
    @staticmethod
    def create_many():
        datas = [
            {"label":"TODO"},
            {"label": "PROGRESS"},
            {"label": "DONE"},
        ]
        entities = []
        for data in datas:
            entities.append(Status.objects.create(**data))
        return entities

class PriorityDBFiller:
    @staticmethod
    def create_many():
        datas = [
            {"label":"URGENT"},
            {"label":"HIGH"},
            {"label":"MEDIUM"},
            {"label":"LOW"},
        ]
        entities = []
        for data in datas:
            entities.append(Priority.objects.create(**data))
        return entities

class ProjectDBFiller:
    @staticmethod
    def create_many():
        datas = [
            {"name":"Project 2"},
            {"name":"Project 3"},
            {"name":"Project 1"},
        ]
        entities = []
        for data in datas:
            entities.append(Project.objects.create(**data))
        return entities