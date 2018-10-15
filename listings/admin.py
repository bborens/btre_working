from django.contrib import admin

from .models import Listing 

# Relates to how Admin table is displayed. !!
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')

admin.site.register(Listing, ListingAdmin)
