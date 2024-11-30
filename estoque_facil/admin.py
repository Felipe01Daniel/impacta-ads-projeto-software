from django.contrib import admin
from .models import Categoria,  Produto, UserProfile, Customer

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Produto)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'status', 'profile_picture')
    search_fields = ('user__username',)

admin.site.register(UserProfile, UserProfileAdmin)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_customer_type', 'email', 'created_at')
    list_filter = ('type',)
    search_fields = ('name', 'email', 'cpf', 'cnpj')
    ordering = ('id',)

    def get_customer_type(self, obj):
        return dict(Customer.TYPE_CHOICES).get(obj.type, 'Desconhecido')
    get_customer_type.short_description = 'Tipo de Cliente'