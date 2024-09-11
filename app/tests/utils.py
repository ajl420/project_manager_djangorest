from app.models import Status, Priority


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
