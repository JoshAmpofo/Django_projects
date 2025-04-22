from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user and a post for testing
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()
        
        # post
        test_post = Post.objects.create(title='Test Post', author=testuser1, body='This is a test post.')
        test_post.save()
        
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Test Post')
        self.assertEqual(body, 'This is a test post.')