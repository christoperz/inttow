from django.db import models
from .num2worlds import say_number

"""Table model to save given number in db"""

class Number(models.Model):
    given_number = models.IntegerField(default=1)


    @property
    def number_in_word(self):
        return say_number(self.given_number)

