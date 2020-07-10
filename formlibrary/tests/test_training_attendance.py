from django.test import TestCase
from formlibrary.models import Individual


class IndividualTestCase(TestCase):

    fixtures = [
        # 'fixtures/tests/organization.json',
        'fixtures/tests/trainings.json',
        # 'fixtures/tests/programs.json',
        # 'fixtures/tests/offices.json',
        'fixtures/tests/users.json',
        'fixtures/tests/activity-users.json',
    ]

    def setUp(self):
        individual = Individual.objects.create(
            first_name="JoeFirst", last_name="JoeLast", age="42",
            sex="Male", signature=False)
        individual.save()

    def test_individual_exists(self):
        """Check for the Individual object"""
        get_individual = Individual.objects.get(first_name="JoeFirst")
        self.assertEqual(Individual.objects.filter(
            id=get_individual.id).count(), 1)
