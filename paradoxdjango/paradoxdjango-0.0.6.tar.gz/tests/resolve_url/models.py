"""
Regression tests for the resolve_url function.
"""

from paradoxdjango.db import models


class UnimportantThing(models.Model):
    importance = models.IntegerField()

    def get_absolute_url(self):
        return "/importance/%d/" % self.importance
