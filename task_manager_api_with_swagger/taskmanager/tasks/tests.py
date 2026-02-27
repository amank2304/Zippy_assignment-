from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task


class TaskAPITest(APITestCase):

    def setUp(self):
        # Regular user
        self.user = User.objects.create_user(username='user1', password='1234')

        # Another user
        self.user2 = User.objects.create_user(username='user2', password='1234')

        # Admin user
        self.admin = User.objects.create_user(username='admin', password='1234', is_staff=True)

        # Create tasks
        self.task1 = Task.objects.create(title="Task 1", description="Desc", user=self.user)
        self.task2 = Task.objects.create(title="Task 2", description="Desc", user=self.user2)

    def authenticate(self, user):
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    # Test List Tasks
    def test_list_tasks_regular_user(self):
        self.authenticate(self.user)
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    # Test Admin Can See All Tasks
    def test_list_tasks_admin(self):
        self.authenticate(self.admin)
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

    # Test Retrieve Task
    def test_retrieve_task(self):
        self.authenticate(self.user)
        response = self.client.get(f"/api/tasks/{self.task1.id}/")
        self.assertEqual(response.status_code, 200)

    # Test Update Task
    def test_update_task(self):
        self.authenticate(self.user)
        response = self.client.put(
            f"/api/tasks/{self.task1.id}/",
            {"title": "Updated", "description": "New", "completed": True}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Updated")

    # Test Delete Task
    def test_delete_task(self):
        self.authenticate(self.user)
        response = self.client.delete(f"/api/tasks/{self.task1.id}/")
        self.assertEqual(response.status_code, 204)

    # Test Unauthorized Access
    def test_unauthorized_access(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 401)

    # Test User Cannot Access Other User Task
    def test_user_cannot_access_other_task(self):
        self.authenticate(self.user)
        response = self.client.get(f"/api/tasks/{self.task2.id}/")
        self.assertEqual(response.status_code, 404)