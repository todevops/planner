from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    # list_filter = ['']
    search_fields = ['username']
    list_display = ('username', 'last_name', 'first_name', 'gender', 'mobile', 'email')
