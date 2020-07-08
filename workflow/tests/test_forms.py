#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.test import TestCase
from workflow.models import (
    Organization, Program, Country, Province, ProjectAgreement, Sector,
    ProjectComplete, ProjectType, SiteProfile, Office, Budget,
    Documentation, Checklist, ProjectStatus
)

def ProgramFormTestCase(TestCase):
    def setUp(self):
        Program.objects.create(name="Natetest")

    def test_create_program(self):
        me = Program.objects.get(name="Natetest")
        self.assertEqual(me.name, 'Natetest2')