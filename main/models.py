from django.db import models

class Vote(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    range1 = models.IntegerField('Семья')
    range2 = models.IntegerField('Друзья')
    range3 = models.IntegerField('Работа')
    range4 = models.IntegerField('Хобби')
    range5 = models.IntegerField('Финансы')
    range6 = models.IntegerField('Спорт и здоровье')
    range7 = models.IntegerField('Саморазвитие')
