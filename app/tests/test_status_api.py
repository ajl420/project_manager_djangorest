from django.db import connection
from rest_framework.test import APITestCase

from app.models import Status
from app.serializers.task_serializer import StatusSerializer
from app.tests.utils import StatusDBFiller


class StatusApiTests(APITestCase):
    def test_create(self):
        invalid_data = { "title": "blabla"}
        response = self.client.post("/api/task-status/", data=invalid_data)
        self.assertEqual(response.status_code, 400)
        valid_data = { "label": "DONE"}
        response = self.client.post("/api/task-status/", data=valid_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["label"], "DONE")

    def test_get(self):
        status_created = StatusDBFiller.create_many()
        status_created_serialized = StatusSerializer(status_created, many=True).data
        response = self.client.get("/api/task-status/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, status_created_serialized)

    def test_update(self):
        StatusDBFiller.create_many()
        update_data = { "label": "TESTED"}
        response = self.client.put("/api/task-status/1", data=update_data)
        updated_data = Status.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Donnee mis a jour!")
        self.assertEqual(updated_data.label, "TESTED")

    def test_delete(self):
        response = self.client.delete("/api/task-status/1")
        self.assertEqual(response.status_code, 404)
        StatusDBFiller.create_many()
        response = self.client.delete("/api/task-status/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Supprime avec success!")

    def setUp(self):
        Status.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE app_status_id_seq RESTART WITH 1;")
