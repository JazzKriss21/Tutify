from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
	list_display = ('username','email','date_joined', 'last_login', 'is_admin','is_staff','user_type')
	search_fields = ('username','email',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)