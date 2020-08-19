from django.test import TestCase

# Create your tests here.
class testApriori(TestCase):
	
	@classmethod
	def setUpData():
		pass
		
	def test_link(self):
		response = self.client.get('/apriori/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'hello.html')
		self.assertNotContains(response,'{{x}}')
		self.assertNotContains(response,'{{y}}')
		self.assertNotContains(response,'{{z}}')
		self.assertContains(response,'table')
	
