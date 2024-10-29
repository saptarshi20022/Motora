from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Mechanic, Booking


admin.site.site_header="Mechanic Booking Administration"
admin.site.site_title="Administration"
admin.site.index_title="Mechanic Booking"
admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
@admin.register(Mechanic)
class MechanicFormAdmin(admin.ModelAdmin):
    list_display=('name','mobile','address','vehicle','specialization','yoe')
    search_fields=('name','mobile')

@admin.register(Booking)
class BookingFormAdmin(admin.ModelAdmin):
    autocomplete_fields = ['mechanic']
    list_display = ('client', 'mobile', 'servicingDate', 'bookingDate', 'name', 'brand', 'modelname', 'serviceDescriptions')

    def client(self, obj):
        return obj.user.first_name+" "+obj.user.last_name

    def name(self, obj):
        return obj.mechanic.name

    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'mechanic':
    #         return BookingFormAdmin(queryset=Mechanic.objects.all())
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)