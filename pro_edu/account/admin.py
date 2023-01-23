from django.contrib import admin
from .models import User,Customer
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    exclude = ('password',)
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_superuser','phone')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_superuser',)
    readonly_fields = ('email',)
    list_editable = ('first_name', 'last_name','phone')


admin.site.register(User, CustomUserAdmin)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user_first_name','user_last_name','user_email','user_phone','user_gender','active','tutor']
    list_editable = ['active']
    list_select_related = ['user']
    list_per_page = 20
    empty_value_display = 'unknown'

    def user_first_name(self,customer):
        return customer.user.first_name

    def user_last_name(self, customer):
        return customer.user.last_name

    def user_gender(self, customer):
        return customer.user.gender

    def user_email(self, customer):
        return customer.user.email

    def user_phone(self, customer):
        return customer.user.phone







