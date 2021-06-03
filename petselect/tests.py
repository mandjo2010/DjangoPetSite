from django.test import TestCase
from .models import Pet
# Create your tests here.

class PetModelTests(TestCase):
    def setUp(self):
        Pet.objects.create(name='toto', hair='short', size='small')

    def test_dog_hair_length(self):
        chi = Pet.objects.get(name='toto')
        self.assertEqual(chi.hair, 'short')
