from django.utils import unittest
from django.test.client import RequestFactory


from djadmin2 import apiviews
from ..models import Post


class ViewTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()


class IndexViewModelListCreateAPIViewTest(ViewTest):
    def test_response_ok(self):
        request = self.factory.get('/admin/api/blog/post/')
        response = apiviews.ListCreateAPIView.as_view(model=Post)(request)
        self.assertEqual(response.status_code, 200)
