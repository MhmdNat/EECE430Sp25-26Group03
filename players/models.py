from django.db import models


class VoleyPlayer(models.Model):
    POSITION_SETTER = "Setter"
    POSITION_LIBERO = "Libero"
    POSITION_MIDDLE_BLOCKER = "Middle Blocker"
    POSITION_OUTSIDE_HITTER = "Outside Hitter"
    POSITION_OPPOSITE = "Opposite"

    POSITION_CHOICES = [
        (POSITION_SETTER, "Setter"),
        (POSITION_LIBERO, "Libero"),
        (POSITION_MIDDLE_BLOCKER, "Middle Blocker"),
        (POSITION_OUTSIDE_HITTER, "Outside Hitter"),
        (POSITION_OPPOSITE, "Opposite"),
    ]

    name = models.CharField(max_length=100)
    dateJoined = models.DateField()
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contactPerson = models.CharField(max_length=100)

    def __str__(self):
        return self.name
