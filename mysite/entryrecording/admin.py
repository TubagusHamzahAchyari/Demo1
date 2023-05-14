from django.contrib import admin
from .models import Customer, CustomerData, Purchase

class CustomerDataAdmin(admin.ModelAdmin):
    list_display = ['customer_number', 'name', 'phone', 'email', 'address', 'postal_zip', 'region', 'country']
    list_filter = ['region', 'country']
    search_fields = ['name', 'email', 'region', 'address']
    list_editable = ['phone']
    list_display_links = ['customer_number']
    def __str__(self):
        return self.name


admin.site.register(Customer)
admin.site.register(CustomerData, CustomerDataAdmin)
admin.site.register(Purchase)


