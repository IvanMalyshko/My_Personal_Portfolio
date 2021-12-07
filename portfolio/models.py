from django.db import models
# СОЗДАНИЕ МОДЕЛИ ПОРТФОЛИО
class Project(models.Model):
    title = models.CharField(max_length=100) # длинна заголовка
    description = models.CharField(max_length=250) # длинна текста
    image = models.ImageField(upload_to='portfolio/images/') # для имаджей с указанием где сохранять и размеров
    url = models.URLField(blank=True) # blank = true это по клику на новую страницу

    def __str__(self): # функция отобразит вместо blog его название
        return self.title

