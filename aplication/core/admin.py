from django.contrib import admin

# Register your models here.
from django.contrib import admin
from aplication.core.models import Doctor, Profession, License, Clinic, Medicamento

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Profession)
admin.site.register(License)
admin.site.register(Clinic)
admin.site.register(Medicamento)


