from .models import City,Room,Low,High,User,Support
from django.forms import ModelForm,TextInput,Textarea

#Классы форм заполнения бд
class CityForm(ModelForm):
    class Meta:
        model=City
        fields=["city"]

        widgets={
                "city":TextInput(attrs={'class':"form-control",
                                        'id':"city",
                                        'type':"text",
                                        'placeholder':"Вологда"})
                                                                   
                 }



class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields=["room"]

        widgets={
                "room":TextInput(attrs={'class':"form-control",
                                     'id':"s",
                                     'type':"number",
                                     'placeholder':"1"})
                                                                   
                 }


class LowForm(ModelForm):
    class Meta:
        model=Low
        fields=["price_low"]

        widgets={
                "price_low":TextInput(attrs={'class':"form-control",
                                         'id':"price_low",
                                        'type':"number",
                                        'min':"0",
                                        'placeholder':"3500000"})
                                                                   
                 }

class HighForm(ModelForm):
    class Meta:
        model=High
        fields=["price_high"]

        widgets={
                "price_high":TextInput(attrs={'class':"form-control",
                                         'id':"price_high",
                                         'type':"number",
                                         'min':"0",
                                        'placeholder':"4500000"})
                                                                   
                 }

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=["email","pasword",]

        widgets={
                "email":TextInput(attrs={'class':"form-control",
                                        'type':"email",
                                        'id':"floatingInput",
                                        'placeholder':"name@example.com"}),
                "pasword":TextInput(attrs={'class':"form-control",
                                            'type':"password",
                                            'id':"floatingPassword",
                                          'placeholder':"Password"})
                 }
        

        
class SupportForm(ModelForm):
    class Meta:
        model=Support
        fields=["tema","main",]

        widgets={
                "tema":TextInput(attrs={'class':"form-control",
                                        'type':"text",
                                        'id':"tema",
                                        'placeholder':"Тема проблемы"}),
                "main":Textarea(attrs={'class':"form-control ",
                                            'id':"main",
                                          'placeholder':"Опишите проблему"})
                 }