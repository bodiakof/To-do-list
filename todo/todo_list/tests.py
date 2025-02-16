from django.test import TestCase
from django.urls import reverse

from todo_list.models import Task, Tag


class TaskModelTests(TestCase):
    def test_create_task(self) -> None:
        tag = Tag.objects.create(name="Test Tag")
        task = Task.objects.create(content="Test Task")
        task.tags.add(tag)
        self.assertEqual(task.content, "Test Task")
        self.assertFalse(task.is_done)
        self.assertIn(tag, task.tags.all())

    def test_toggle_task_status(self) -> None:
        task = Task.objects.create(content="Test Task")
        self.assertFalse(task.is_done)
        task.is_done = not task.is_done
        task.save()
        self.assertTrue(task.is_done)


class TagModelTests(TestCase):
    def test_create_tag(self) -> None:
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(tag.name, "Test Tag")


class TaskViewTests(TestCase):
    def test_home_page(self) -> None:
        response = self.client.get(reverse("todo_list:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TODO List")

    def test_add_task(self) -> None:
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.post(reverse("todo_list:add_task"), {
            "content": "New Task",
            "deadline": "",
            "tags": [tag.pk],
            "is_done": False
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content="New Task").exists())

    def test_update_task(self) -> None:
        tag = Tag.objects.create(name="Test Tag")
        task = Task.objects.create(content="Old Task")
        response = self.client.post(reverse("todo_list:update_task", args=[task.pk]), {
            "content": "Updated Task",
            "deadline": "",
            "tags": [tag.pk],
            "is_done": False
        })
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.content, "Updated Task")

    def test_delete_task(self) -> None:
        task = Task.objects.create(content="Test Task")
        response = self.client.post(reverse("todo_list:delete_task", args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_toggle_task_status(self) -> None:
        task = Task.objects.create(content="Test Task")
        response = self.client.post(reverse("todo_list:toggle_task_status", args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertTrue(task.is_done)


class TagViewTests(TestCase):
    def test_tag_list_page(self) -> None:
        response = self.client.get(reverse("todo_list:tag_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tags")

    def test_add_tag(self) -> None:
        response = self.client.post(reverse("todo_list:add_tag"), {
            "name": "New Tag"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())

    def test_update_tag(self) -> None:
        tag = Tag.objects.create(name="Old Tag")
        response = self.client.post(reverse("todo_list:update_tag", args=[tag.pk]), {
            "name": "Updated Tag"
        })
        self.assertEqual(response.status_code, 302)
        tag.refresh_from_db()
        self.assertEqual(tag.name, "Updated Tag")

    def test_delete_tag(self) -> None:
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.post(reverse("todo_list:delete_tag", args=[tag.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(pk=tag.pk).exists())
