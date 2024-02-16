from django.contrib import admin

from accounts_users.models import AppUser, ProfileUser


# Register your models here.
@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    pass
