from django.contrib import admin
from api.models import User,Profile,webtoons,Comment,Favorite

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name' ,'verified']

admin.site.register(User, UserAdmin)
admin.site.register( Profile,ProfileAdmin)
admin.site.register(webtoons)
admin.site.register(Comment)
admin.site.register(Favorite)


