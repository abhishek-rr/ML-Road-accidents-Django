from django.test import TestCase

# Create your tests here.
class testKMeans(TestCase):
	@classmethod
	def setUpData():
		pass
		
	def test_link(self):
		response = self.client.get('/kmeans/')
		self.assertEqual(response.status_code,200)
		self.assertNotContains(response,'{{fig1|safe}}')
		self.assertNotContains(response,'{{fig2|safe}}')
