from django.db import models
from datetime import date
from database.models import Medicines
from client.models import Client

class Orders(models.Model):
    medicines = models.ForeignKey(Medicines, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    registration_date = models.DateField('Время регистрации', default=date.today)
    extradition_date = models.DateField('Время выдачи')
    received = models.BooleanField('Получин', default=False)

    def __str__(self):
        return self.client.surname + " " + self.client.name + " " +  self.client.patronymic + " | " + self.medicines.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'