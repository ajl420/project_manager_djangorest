from app.models import Status, Priority, Project, Task


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

class TaskDBFiller:
    @staticmethod
    def create_many():
        StatusDBFiller.create_many()
        PriorityDBFiller.create_many()
        ProjectDBFiller.create_many()
        datas = [
            {
                'name': 'Test Task 1',
                'description': 'Test description',
                'status_id': 1,
                'priority_id': 1,
                'project_id': 1,
            },
            {
                'name': 'Test Task 2',
                'description': 'Test description',
                'status_id': 2,
                'priority_id': 3,
                'project_id': 2,
            },
            {
                'name': 'Test Task 3',
                'description': 'Test description',
                'status_id': 1,
                'priority_id': 1,
                'project_id': 2,
            },
            {
                'name': 'Test Task 4',
                'description': 'Test description',
                'status_id': 1,
                'priority_id': 1,
                'project_id': 2,
            },
            {
                'name': 'Test Task 5',
                'description': 'Test description',
                'status_id': 1,
                'priority_id': 1,
                'project_id': 1,
            },
            {
                'name': 'Test Task 6',
                'description': 'Test description',
                'status_id': 1,
                'priority_id': 2,
                'project_id': 2,
            },
            {
                'name': 'Test Task 7',
                'description': 'Test description',
                'status_id': 1,
                'priority_id': 1,
                'project_id': 2,
            },
            {
                'name': 'Test Task 8',
                'description': 'Test description',
                'status_id': 1,
                'priority_id': 2,
                'project_id': 2,
            },
        ]
        entities = []
        for data in datas:
            entities.append(Task.objects.create(**data))
        return entities
