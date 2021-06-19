from django.contrib import admin

# Register your models here.
from .models import Bin, Operation, Execution

admin.site.register(Bin)
admin.site.register(Operation)
admin.site.register(Execution)
