from django.contrib import admin

from recipie.models import Recipie,Review_or_Comment

# Register your models here.


admin.site.register(Recipie)
admin.site.register(Review_or_Comment)
