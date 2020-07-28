from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Planet:{self.id}>"
