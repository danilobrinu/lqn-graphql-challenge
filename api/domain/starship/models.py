from django.db import models


class Starship(models.Model):
    name = models.CharField(max_length=100)
    length = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Starship:{self.id}>"
