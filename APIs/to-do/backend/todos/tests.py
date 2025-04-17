from django.test import TestCase
from .models import Todo
# Create your tests here

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Todo object for testing
        Todo.objects.create(title="Test Todo", body="This is a test todo item.")
        
    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'Test Todo')
        
    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEqual(expected_object_name, 'This is a test todo item.')