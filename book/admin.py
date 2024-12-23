from django.contrib import admin

from .models import Otdel, Building, Person

class Person_Admin(admin.ModelAdmin):
    fieldsets = [
            ('Расположение', {'fields': [('Otdel','Building'), ('Floor', 'Room')]}),
            ('Сотрудник', {'fields': ['SurName','FirstName','Patronymic', 'Post', 'Number_in', 'Number_ext']}),
            ]
    list_display = ('Otdel','Building','SurName', 'FirstName', 'Number_in', 'Number_ext')
    search_fields = ['SurName', 'Otdel__Name']
    list_filter = ['Otdel', 'Building']
    list_per_page = 20
    view_on_site = True
    verbose_name = 'Сотрудник'



#admin.site.register(Location, Phone_book_Admin)
admin.site.register(Otdel)
admin.site.register(Building)
admin.site.register(Person, Person_Admin)
#admin.site.register(Location)
