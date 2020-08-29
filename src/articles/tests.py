import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Article, Comments, Favourite


class QuestionModelTests(TestCase):

    def test_register_accounts(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)