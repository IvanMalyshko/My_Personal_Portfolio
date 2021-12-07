from django.db import models
# СОЗДАНИЕ МОДЕЛИ БЛОГА
class Blog(models.Model):
    title = models.CharField(max_length=250) # длинна заголовка
    description = models.TextField() # длинна текста
    date = models.DateField() # добавляем дату

    def __str__(self): # функция отобразит вместо blog его название
        return self.title
