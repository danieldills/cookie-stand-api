from django.contrib import admin
from .models import CookieStand

# Register your models here.
@admin.register(CookieStand)
class AdminForConcert(admin.ModelAdmin):
    list_display = ("location", "owner", "created_at")
    # prepopulated_fields = {
    #     "slug": ("title",),
    # }


# admin.site.register(AnotherModel)
