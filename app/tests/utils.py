from app.models import Status


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
