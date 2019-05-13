# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Question
import datetime
from django.utils import timezone

# Create your tests here.

class QuestionModelTest(TestCase):
	def test_was_published_recently_with_future_question(self):

		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)
