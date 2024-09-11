from http.client import responses

from django.db import connection
from rest_framework.test import APITestCase

from app.models import Priority
from app.serializers.task_serializer import PrioritySerializer
from app.tests.utils import PriorityDBFiller


class PriorityApiTests(APITestCase):
    def test_create(self):
        invalid_data = { "title": "blabla"}
        response = self.client.post("/api/task-priorities/", data=invalid_data)
        self.assertEqual(response.status_code, 400)
        valid_data = { "label": "URGENT"}
        response = self.client.post("/api/task-priorities/", data=valid_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["label"], "URGENT")
        self.assertEqual(response.data["level"], 1)

    def test_get(self):
        priorities_created = PriorityDBFiller.create_many()
        priorities_created_serialized = PrioritySerializer(priorities_created, many=True).data
        response = self.client.get("/api/task-priorities/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, priorities_created_serialized)

    def test_update(self):
        PriorityDBFiller.create_many()
        update_data = { "label": "MAIKA" }
        response = self.client.put("/api/task-priority/1", data=update_data)
        updated_data = Priority.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Donnee mis a jour!")
        self.assertEqual(updated_data.label, "MAIKA")
    #
    def test_delete(self):
        response = self.client.delete("/api/task-priority/1")
        self.assertEqual(response.status_code, 404)
        PriorityDBFiller.create_many()
        response = self.client.delete("/api/task-priority/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Supprime avec success!")

    def test_switch(self):
        PriorityDBFiller.create_many()
        data = {
            "first_priority_level": 1,
            "second_priority_level": 2,
        }
        response = self.client.put("/api/task-priorities-switch-level/", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Donnee mis a jour!")
        p1 = Priority.objects.get(pk=1)
        p2 = Priority.objects.get(pk=2)
        self.assertEqual(p1.label, "HIGH" )
        self.assertEqual(p2.label, "URGENT")

    def setUp(self):
        Priority.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE app_priority_level_seq RESTART WITH 1;")