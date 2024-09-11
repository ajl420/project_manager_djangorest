from cProfile import label
from http.client import responses

from django.db import connection
from rest_framework.test import APITestCase
from app.models import Status, Project, Task, Priority
from app.serializers.task_serializer import TaskSerializer
from app.tests.utils import TaskDBFiller


class TestTaskAPI(APITestCase):

    def test_create(self):
        valid_data = {
            'name': 'Test Task',
            'description': 'Test description',
            'status_id': 1,
            'priority_id': 1,
        }
        response = self.client.post('/api/project/1/tasks/', data=valid_data)
        self.assertEqual(response.status_code, 404)
        project = Project.objects.create(name='Test Project')
        response = self.client.post('/api/project/1/tasks/', data=valid_data)
        self.assertEqual(response.status_code, 404)
        status = Status.objects.create(label='TODO')
        priority = Priority.objects.create(label='HIGH')
        response = self.client.post('/api/project/1/tasks/', data=valid_data)
        task = response.data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(task['name'], 'Test Task')
        self.assertEqual(task['description'], 'Test description')
        self.assertEqual(task['status']['label'], status.label)
        self.assertEqual(task['priority']['label'], priority.label)
        self.assertEqual(task['project']['name'], project.name)

    def test_retrieve(self):
        TaskDBFiller.create_many()
        response = self.client.get('/api/project/1/task/2')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], "Ce/cette projet n'appartient pas a ce/cette tache")
        response = self.client.get('/api/project/2/task/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Task 2')

    def test_delete(self):
        TaskDBFiller.create_many()
        response = self.client.delete('/api/project/1/task/2')
        self.assertEqual(response.status_code, 400)
        response = self.client.delete('/api/project/2/task/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], "Suppression avec success!")

    def test_list(self):
        TaskDBFiller.create_many()
        response = self.client.get('/api/project/2/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 6)

    def test_filter_fail(self):
        TaskDBFiller.create_many()
        response = self.client.get('/api/project/2/tasks/?filter_by=name&filter_value=1')
        self.assertEqual(response.status_code, 400)

    def test_filter_by_status(self):
        TaskDBFiller.create_many()
        response = self.client.get('/api/project/2/tasks/?filter_by=status&filter_value=2')
        self.assertEqual(response.status_code, 200)
        for task in response.data:
            self.assertEqual(task['status']['label'], "PROGRESS")

    def test_filter_by_priority(self):
        TaskDBFiller.create_many()
        response = self.client.get('/api/project/2/tasks/?filter_by=priority&filter_value=1')
        self.assertEqual(response.status_code, 200)
        for task in response.data:
            self.assertEqual(task['priority']['label'], "URGENT")

    def setUp(self):
        Status.objects.all().delete()
        Project.objects.all().delete()
        Task.objects.all().delete()
        Priority.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE app_status_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE app_project_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE app_priority_level_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE app_task_id_seq RESTART WITH 1;")

