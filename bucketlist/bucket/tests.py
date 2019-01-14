from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class BucketIndexViewTests(TestCase):
    def test_no_bucket(self):

        response = self.client.get(reverse('buckets:index'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['bucket_list'], [])
        