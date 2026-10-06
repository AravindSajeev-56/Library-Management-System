from django.contrib import admin

# Register your models here.


from .models import books
from .models import Bookingbooks

class booksAdmin(admin.ModelAdmin):
    pass
admin.site.register(books,booksAdmin)

class BookingbooksAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bookingbooks,BookingbooksAdmin)