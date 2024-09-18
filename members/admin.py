from django.contrib import admin
from .models import Member


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date", "court__time_of_occupation")


admin.site.register(Member, MemberAdmin)
