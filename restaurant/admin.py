from django.contrib import admin
from restaurant.models import Menu, Booking

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')
    search_fields = ('title',)
    list_filter = ('price',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests', 'booking_date')
    search_fields = ('name',)
    list_filter = ('booking_date',)

admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)