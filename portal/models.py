from django.db import models


class CardData(models.Model):
    card_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    card_cvc = models.CharField(max_length=255)
    card_expirationDate = models.CharField(max_length=255)

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name = 'Card Data'
        verbose_name_plural = 'Cards Data'