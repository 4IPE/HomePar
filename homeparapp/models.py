from django.db import models
#Класс по созданию бд Города 
class City(models.Model):
    city=models.CharField('Адрес',max_length=250)

    def __str__(self):
        return self.city
    
#Класс по созданию бд кол-во комнат 
class Room (models.Model):
    room=models.CharField('s',max_length=15)


    def __str__(self):
        return self.room
    
#Класс по созданию бд минимальной стоимости      
class Low(models.Model):
    price_low=models.CharField('Цена от',max_length=15)


    def __str__(self):
        return self.price_low
#Класс по созданию бд максимальной стоимости  
class High(models.Model):
    price_high=models.CharField('Цена до',max_length=15)


    def __str__(self):
        return self.price_high
    

#Класс по созданию бд Аккаунтов
class User(models.Model):
    email=models.CharField('email',max_length=250)
    pasword=models.CharField('pasword',max_length=250)


    def __str__(self):
        return self.email


#Класс по созданию бд вопросов
class Support(models.Model):
    tema=models.CharField('Tema',max_length=250)
    main=models.CharField('Описание',max_length=1000)


    def __str__(self):
        return self.tema