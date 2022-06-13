from django.test import TestCase
from django.core.management import call_command

class PoblarDb(TestCase):
    def setUp(self) -> None:
        call_command('reset_db', '--noinput')

    def tearDown(self) -> None:
        call_command('reset_db', '--noinput')

    def test_poblar_db(self):
        call_command('generar_todo')