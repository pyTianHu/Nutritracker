from django.contrib import admin
from .models import (
    BodyWeight, 
    Goals
    )


# Register your models here.
admin.site.register(BodyWeight)
admin.site.register(Goals)