from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "class_level", "roll_no", "phone_no",'created_date','updated_date')
    # prepopulated_fields = {"slug": ("first_name", "last_name")}
    # formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(Student, StudentAdmin)

