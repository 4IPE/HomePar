from django.contrib import admin
from .models import City,Room,Low,High,User,Support
#Вывод бд в админской панели 
admin.site.register(City)
admin.site.register(Room)
admin.site.register(Low)
admin.site.register(High)
admin.site.register(User)
admin.site.register(Support)
