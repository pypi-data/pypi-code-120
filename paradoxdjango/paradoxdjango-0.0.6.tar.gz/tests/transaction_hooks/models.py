from paradoxdjango.db import models


class Thing(models.Model):
    num = models.IntegerField()
