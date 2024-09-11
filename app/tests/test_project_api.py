from audioop import reverse

from django.db import connection
from rest_framework.test import APITestCase
from .utils import ProjectDBFiller

from app.models import Project
from ..serializers.project_serializer import ProjectSerializer


class ProjectApiTests(APITestCase):
    def test_create(self):
        invalid_data = {"boma":"mabo"}
        response = self.client.post('/api/projects/', data=invalid_data)
        self.assertEqual(response.status_code, 400)
        valid_data = {"name":"project 1"}
        response = self.client.post('/api/projects/', data=valid_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "project 1")

    def test_update(self):
        ProjectDBFiller.create_many()
        update_data = {"name":"project 2"}
        response = self.client.put('/api/project/1', data=update_data)
        updated_data = Project.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_data.name, "project 2")

    def test_list(self):
        projects = ProjectDBFiller.create_many()
        projects_serialized = ProjectSerializer(projects, many=True).data
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, projects_serialized)

    def test_list_sorted_by_name(self):
        projects = ProjectDBFiller.create_many()
        projects_serialized = ProjectSerializer(projects, many=True).data
        response = self.client.get('/api/projects/?order_by=foo')
        self.assertEqual(response.status_code, 400)
        response = self.client.get('/api/projects/?order_by=name')
        self.assertEqual(response.status_code, 200)
        projects_serialized = sorted(projects_serialized, key=lambda x: x["name"])
        self.assertEqual(response.data, projects_serialized)

    def test_list_sorted_by_date(self):
        projects = ProjectDBFiller.create_many()
        projects.reverse()
        projects_serialized = ProjectSerializer(projects, many=True).data
        response = self.client.get('/api/projects/?order_by=created_at')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, projects_serialized)
        projects_serialized.reverse()
        self.assertEqual(response.data, projects_serialized)

    def test_delete(self):
        response = self.client.delete('/api/project/1')
        self.assertEqual(response.status_code, 404)
        ProjectDBFiller.create_many()
        response = self.client.delete('/api/project/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Supprime avec success!")
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(pk=1)

    def setUp(self):
        Project.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE app_project_id_seq RESTART WITH 1;")