from django.contrib import admin
from .models import Categoria,  Produto, UserProfile

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Produto)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'status', 'profile_picture')
    search_fields = ('user__username',)

admin.site.register(UserProfile, UserProfileAdmin)